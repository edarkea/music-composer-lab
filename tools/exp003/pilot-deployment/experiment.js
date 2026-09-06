/* EXP-003 participant-interface instrumentation. jsPsych 8.2.1. */
(async () => {
  const PRE_DELAY_MS = 1000;
  const INTER_TRIAL_MS = 1000;
  const SCALE = [1, 2, 3, 4, 5, 6, 7];
  const LABELS = {
    1: "distancia musical muy pequeña",
    4: "distancia musical intermedia",
    7: "distancia musical muy grande",
  };
  const LIST_A = {F01:"LOW",F02:"HIGH",F03:"LOW",F04:"LOW",F05:"HIGH",F06:"HIGH",F07:"LOW",F08:"HIGH",F09:"HIGH",F10:"HIGH",F11:"LOW",F12:"LOW"};
  const LIST_B = Object.fromEntries(Object.entries(LIST_A).map(([f,c]) => [f,c === "LOW" ? "HIGH" : "LOW"]));
  const ORDERS = {
    O1: ["F03","F10","F01","F08","F12","F05","F07","F02","F11","F06","F04","F09"],
    O2: ["F09","F04","F06","F11","F02","F07","F05","F12","F08","F01","F10","F03"],
    O3: ["F08","F12","F05","F07","F02","F11","F06","F04","F09","F03","F10","F01"],
  };
  const params = new URLSearchParams(location.search);
  const cell = params.get("cell") || "A-O1";
  const [assignment_list, order_sequence] = cell.split("-");
  if (!ORDERS[order_sequence] || !["A","B"].includes(assignment_list)) throw new Error("invalid operational cell");
  const mapping = await fetch("mapping.private.json", {cache: "no-store"}).then(r => { if (!r.ok) throw Error("mapping load failure"); return r.json(); });
  const map = mapping.entries;
  if (!Array.isArray(map) || map.length !== 27) throw new Error("mapping cardinality failure");
  const assignment = assignment_list === "A" ? LIST_A : LIST_B;
  const trials = ORDERS[order_sequence].map((family, index) => {
    const condition = assignment[family];
    const item = map.find(x => x.family_id === `EXP003-${family}` && x.condition === `${condition}_SELECTED`);
    if (!item) throw new Error("opaque mapping failure");
    return { ...item, serial_position: index + 1 };
  });
  const jsPsych = initJsPsych({on_finish: () => {
    window.__EXP003_DRY_RUN_EXPORT__ = jsPsych.data.get().values();
    window.__EXP003_DRY_RUN_COMPLETE__ = true;
  }});
  const mark = (record_type, extra = {}) => ({data: {record_type, pilot_stage: "STAGE_1_DRY_RUN", assignment_list, order_sequence, ...extra}});
  const delay = (duration) => ({type: jsPsychHtmlButtonResponse, stimulus: "", choices: [], trial_duration: duration, response_ends_trial: false, data: {record_type: "INTERFACE_DELAY"}});
  const choices = SCALE.map(String);
  const button_html = (choice) => `<button class="jspsych-btn distance-choice">${choice}<small>${LABELS[choice] || "&nbsp;"}</small></button>`;
  const rating_trial = (item, record_type) => ({
    type: jsPsychAudioButtonResponse,
    stimulus: item.opaque_audio_path,
    choices,
    button_html,
    prompt: `<div class="distance-question">¿Qué tan grande te parece la distancia musical entre la primera y la segunda sonoridad?</div>`,
    response_allowed_while_playing: false,
    response_ends_trial: true,
    trial_ends_after_audio: false,
    data: {record_type, internal_family_id: item.family_id, condition: item.condition, canonical_asset_sha256: item.wav_sha256, canonical_asset_reference: item.canonical_wav_path, opaque_presentation_id: item.opaque_presentation_id, serial_position: item.serial_position || null, playback_started: false, playback_completed: false, response_recorded: false},
    on_load: () => { const audio = document.querySelector("audio"); if (audio) { audio.addEventListener("play", () => { jsPsych.data.addDataToLastTrial({playback_started: true}); }); audio.addEventListener("ended", () => { jsPsych.data.addDataToLastTrial({playback_completed: true}); }); } },
    on_finish: data => { data.playback_started = true; data.playback_completed = true; data.rating_1_7 = data.response === null ? null : data.response + 1; data.response_recorded = data.rating_1_7 !== null; data.technical_error = data.rating_1_7 === null ? "missing_response" : null; delete data.response; },
  });
  const timeline = [];
  timeline.push({type: jsPsychHtmlButtonResponse, stimulus: `<h2>Antes de comenzar</h2><p>Usa auriculares para esta tarea.</p><p>¿Confirmas que estás usando auriculares?</p>`, choices: ["Sí, estoy usando auriculares", "No"], data: {record_type: "HEADPHONE_GATE"}, on_finish: data => { if (data.response === 1) jsPsych.endExperiment("La sesión no puede continuar sin auriculares."); }});
  timeline.push({type: jsPsychHtmlButtonResponse, stimulus: `<p>Ajusta el volumen a un nivel cómodo. Primero escucharás un sonido de comprobación.</p>`, choices: ["Continuar"], data: {record_type: "VOLUME_CHECK_READY"}});
  timeline.push(delay(PRE_DELAY_MS));
  const volume = map.find(x => x.internal_asset_id === "DEPLOY-VOLUME-01");
  timeline.push({...rating_trial({...volume, opaque_audio_path: volume.opaque_audio_path, serial_position: null}, "VOLUME_CHECK"), choices: ["Continuar"], prompt: `<div class="audio-note">Comprueba que el nivel sea cómodo y continúa.</div>`, button_html: choice => `<button class="jspsych-btn">${choice}</button>`});
  timeline.push({type: jsPsychHtmlButtonResponse, stimulus: `<h2>Práctica</h2><p>Escucharás dos ejemplos de práctica. No hay respuestas correctas o incorrectas.</p>`, choices: ["Comenzar práctica"], data: {record_type: "PRACTICE_INTRO"}});
  for (const item of map.filter(x => x.record_type === "PRACTICE")) { timeline.push(delay(PRE_DELAY_MS), rating_trial(item, "PRACTICE"), delay(INTER_TRIAL_MS)); }
  timeline.push({type: jsPsychHtmlButtonResponse, stimulus: `<h2>Tarea</h2><p>Escucharás 12 pares de sonoridades. Usa la escala para indicar lo que percibas.</p>`, choices: ["Comenzar tarea"], data: {record_type: "EXPERIMENTAL_INTRO"}});
  for (const item of trials) timeline.push(delay(PRE_DELAY_MS), rating_trial(item, "EXPERIMENTAL"), delay(INTER_TRIAL_MS));
  timeline.push({type: jsPsychSurveyText, questions: [{prompt: "Con tus propias palabras, ¿qué entendiste por ‘distancia musical’ al hacer esta tarea?", rows: 5, columns: 60}], data: {record_type: "POST_TASK_DIAGNOSTIC"}});
  timeline.push({type: jsPsychHtmlButtonResponse, stimulus: "<p>Gracias. La sesión ha terminado.</p>", choices: ["Finalizar"], data: {record_type: "SESSION_COMPLETE"}});
  const audio_paths = map.map(x => x.opaque_audio_path);
  jsPsych.run([{type: jsPsychPreload, audio: audio_paths, continue_after_error: false, data: {record_type: "PRELOAD", preload_status: "PASS"}}, ...timeline]);
})();

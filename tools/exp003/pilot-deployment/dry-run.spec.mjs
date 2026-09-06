import { test, expect } from "@playwright/test";

const cells = ["A-O1", "A-O2", "A-O3", "B-O1", "B-O2", "B-O3"];

async function clickAndWait(page, label) {
  await page.getByRole("button", {name: label}).click();
}

async function completeCell(page, cell) {
  await page.goto(`http://127.0.0.1:8765/?cell=${cell}`);
  await clickAndWait(page, "Sí, estoy usando auriculares");
  await clickAndWait(page, "Continuar");
  const volumeButton = page.getByRole("button", {name: "Continuar"});
  await expect(volumeButton).toBeDisabled();
  await page.waitForTimeout(2300);
  await volumeButton.click();
  await clickAndWait(page, "Comenzar práctica");
  for (let i = 0; i < 2; i++) {
    const choice = page.getByRole("button", {name: "4"});
    await expect(choice).toBeDisabled();
    await page.waitForTimeout(2300);
    await choice.click();
  }
  await clickAndWait(page, "Comenzar tarea");
  for (let i = 0; i < 12; i++) {
    const choice = page.getByRole("button", {name: "4"});
    await expect(choice).toBeDisabled();
    await page.waitForTimeout(2300);
    await choice.click();
  }
  await page.locator("textarea").fill("Prueba técnica del dry-run.");
  await clickAndWait(page, "Continue");
  await clickAndWait(page, "Finalizar");
  await page.waitForTimeout(500);
  console.log("DRY_STATE", await page.evaluate(() => ({complete: window.__EXP003_DRY_RUN_COMPLETE__, exportLength: window.__EXP003_DRY_RUN_EXPORT__?.length, body: document.body.innerText})));
  await expect.poll(() => page.evaluate(() => window.__EXP003_DRY_RUN_COMPLETE__), {timeout: 5000}).toBe(true);
  const data = await page.evaluate(() => window.__EXP003_DRY_RUN_EXPORT__);
  const exp = data.filter(x => x.record_type === "EXPERIMENTAL");
  const practice = data.filter(x => x.record_type === "PRACTICE");
  expect(exp).toHaveLength(12);
  expect(practice).toHaveLength(2);
  expect(exp.every(x => x.rating_1_7 === 4 && x.playback_started && x.playback_completed && x.response_recorded)).toBe(true);
  return {cell, records: data.length, experimental: exp.length, practice: practice.length};
}

for (const cell of cells) {
  test(`EXP-003 dry-run ${cell}`, async ({page}) => {
    test.setTimeout(90000);
    console.log(JSON.stringify(await completeCell(page, cell)));
  });
}

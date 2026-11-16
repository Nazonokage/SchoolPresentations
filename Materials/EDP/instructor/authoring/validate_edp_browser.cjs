const { chromium } = require('C:/Users/Someone/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const { spawn } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve('Application Development and Emerging Technologies (Inluding event Driven programming)/EDP');
const assert = require('node:assert/strict');
(async () => {
  if (process.argv.includes('--visuals-only')) {
    const browser = await chromium.launch({channel:'msedge',headless:true});
    try {
      const page = await browser.newPage({viewport:{width:1366,height:768}});
      const {pathToFileURL}=require('node:url');
      await page.goto(pathToFileURL(path.join(root,'visuals/gallery.html')).href);
      assert.equal(await page.locator('article').count(),20);
      assert.equal(await page.locator('img').evaluateAll(images=>images.every(img=>img.complete && img.naturalWidth>0)),true);
      const before=await page.locator('article p').first().evaluate(el=>parseFloat(getComputedStyle(el).fontSize));
      await page.getByRole('button',{name:'Increase text size'}).click();
      const after=await page.locator('article p').first().evaluate(el=>parseFloat(getComputedStyle(el).fontSize));
      assert.ok(after>before && before>=16);
      await page.screenshot({path:path.join(root,'visuals/gallery-checked.png'),fullPage:false});
      await page.setViewportSize({width:390,height:844});
      await page.getByRole('button',{name:'Reset',exact:true}).click();
      const small=await page.locator('article p').first().evaluate(el=>parseFloat(getComputedStyle(el).fontSize));
      assert.ok(small>=16);
      console.log('Visual gallery passed: 20 SVG loads, larger text control, >=16px body on desktop and narrow viewport.');
    } finally {await browser.close();}
    return;
  }
  const server = spawn(process.execPath, ['server.mjs'], { cwd: path.join(root, 'examples'), windowsHide: true, stdio: ['ignore','pipe','pipe'] });
  let browser;
  try {
    await new Promise((resolve, reject) => {
      const timeout = setTimeout(() => reject(new Error('Server startup timeout')), 10000);
      server.stdout.once('data', () => { clearTimeout(timeout); resolve(); });
      server.once('exit', code => { clearTimeout(timeout); reject(new Error('Server exited: '+code)); });
    });
    browser = await chromium.launch({ channel: 'msedge', headless: true });
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto('http://127.0.0.1:4173/m03-first.html');
    await page.getByRole('button', {name:'Say hello'}).click();
    assert.equal(await page.locator('#message').textContent(), 'Hello, coder! Kaya mo ito.');
    await page.goto('http://127.0.0.1:4173/m03.html');
    await page.getByRole('button', {name:'Say hello'}).click();
    assert.equal(await page.locator('#message').textContent(), 'Hello, coder!');
    await page.locator('#food').fill('   ');
    await page.getByRole('button', {name:'Add order'}).click();
    assert.equal(await page.locator('#orders li').count(), 0);
    await page.locator('#food').fill('Pandesal');
    await page.locator('#food').press('Enter');
    assert.equal(await page.locator('#orders li').count(), 1);
    await page.getByRole('button', {name:'Collected',exact:true}).click();
    assert.equal(await page.locator('#orders li').count(), 0);
    await page.getByRole('button', {name:'Stop listeners'}).click();
    assert.equal(await page.getByRole('button', {name:'Say hello'}).isDisabled(), true);
    await page.screenshot({ path:path.join(root,'instructor/m03-checked.png'),fullPage:true });
    await page.goto('http://127.0.0.1:4173/m08.html');
    await page.locator('#search').fill('library');
    await page.waitForFunction(() => document.querySelector('#result').textContent === 'Results: LIBRARY');
    await page.locator('#search').fill('error');
    await page.waitForFunction(() => document.querySelector('#result').textContent === 'Handled: Search unavailable');
    await page.locator('#search').fill('clinic');
    await page.waitForFunction(() => document.querySelector('#result').textContent === 'Results: CLINIC');
    await page.getByRole('button', {name:'Stop search'}).click();
    assert.equal(await page.locator('#result').textContent(), 'Search stopped.');
    assert.equal(await page.locator('#search').isDisabled(), true);
    await page.screenshot({ path:path.join(root,'instructor/m08-checked.png'),fullPage:true });
    await page.goto('http://127.0.0.1:4173/m09.html');
    await page.waitForFunction(() => document.querySelectorAll('#messages li').length >= 2);
    assert.equal(await page.locator('#status').textContent(), 'Connected');
    await page.getByRole('button', {name:'Disconnect'}).click();
    const count = await page.locator('#messages li').count();
    await page.waitForTimeout(700);
    assert.equal(await page.locator('#messages li').count(), count);
    assert.equal(await page.locator('#status').textContent(), 'Disconnected');
    await page.screenshot({ path:path.join(root,'instructor/m09-checked.png'),fullPage:true });
    assert.deepEqual(errors, []);
    fs.writeFileSync(path.join(root,'instructor/browser-results.json'),JSON.stringify({browser:await browser.version(),passed:true,checks:['M03 minimal first click','M03 click','whitespace rejected','keyboard submit','delegated collection','cleanup disables controls','M08 reactive search','inner error and recovery','unsubscribe disables search','M09 real SSE messages','disconnect stops updates','no page errors']},null,2));
    console.log('Browser checks passed: DOM interaction/cleanup and real SSE/disconnect.');
  } finally {
    if (browser) await browser.close();
    server.kill();
  }
})().catch(error => { console.error(error); process.exitCode=1; });

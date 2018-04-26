const timeout = 5000

describe(
  '/ (Bitcoin Predict)',
  () => {
    let page
    beforeAll(async () => {
      page = await global.__BROWSER__.newPage()
      await page.goto('http://127.0.0.1:8000/')
    }, timeout)

    afterAll(async () => {
      await page.close()
    })

    it('should load without error', async () => {
      let text = await page.evaluate(() => document.body.textContent)
      expect(text).toContain('Bitcoin Predict')
    })
  },
  timeout
)

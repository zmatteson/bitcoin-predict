module.exports = {
    verbose: true,
    "preset": "jest-puppeteer-preset",
    globalSetup: './setup.js',
    globalTeardown: './teardown.js',
    testEnvironment: './puppeteer_environment.js',
  };

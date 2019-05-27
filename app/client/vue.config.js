module.exports = {
  publicPath: './',
  outputDir: '../templates',
  assetsDir: process.env.NODE_ENV === 'production' ? '../static' : ''
}
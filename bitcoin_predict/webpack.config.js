const path = require('path');
const webpack = require('webpack');

module.exports = {
  context: __dirname,
  entry: [
    'react-hot-loader/patch',
    'webpack-dev-server/client?http://localhost:8080',
    'webpack/hot/only-dev-server',
    './bitcoin_predict/static/js/ClientApp.jsx'
	
  ],
  devtool: 'cheap-eval-source-map',
  output: {
    path: path.resolve('./bitcoin_predict/static/bundles/local/'),
    filename: 'bundle.js',
 
  },
  devServer: {
    hot: true,
    publicPath: '/public/',
    historyApiFallback: true
  },
  resolve: {
    extensions: ['.js', '.jsx', '.json']
  },
  stats: {
    colors: true,
    reasons: true,
    chunks: true
  },
  plugins: [new webpack.HotModuleReplacementPlugin(), new webpack.NamedModulesPlugin(), new webpack.optimize.CommonsChunkPlugin({name:'vendors', filename: 'vendors.js' }),],
  module: {
	loaders: [
      { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
      { test: /\.jsx$/, loader: 'babel-loader', exclude: /node_modules/ }
    ],
	
    rules: [
      {
        enforce: 'pre',
        test: /\.jsx?$/,
        loader: 'eslint-loader',
        exclude: /node_modules/
      },
      {
        test: /\.jsx?$/,
        loader: 'babel-loader'
      }
    ]
  },
  resolve: {
    modules: ['node_modules', 'bower_components'],
    extensions: ['.js', '.jsx']
  },

};

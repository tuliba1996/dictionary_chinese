module.exports = {
  // css: {
  //   loaderOptions: {
  //     css: {
  //       data: `
  //         @import "@/assets/styles/global.css";
  //       `,
  //     },
  //   },
  // },
  devServer: {
    proxy: 'http://localhost:8000'
  }
};

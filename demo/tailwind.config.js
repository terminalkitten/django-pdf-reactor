module.exports = {
  purge: [],
  theme: {
    fontFamily: {
      print: ["Verdana", "Arial", "sans-serif"],
    },
    extend: {
      screens: {
        print: { raw: "print" },
      },
      animation: {
        progress: "progress 6s ease-in-out infinite",
      },
      keyframes: {
        progress: {
          "0%": { width: "0%" },
          "100%": { width: "100%" },
        },
      },
    },
  },
  variants: {},
  plugins: [],
};

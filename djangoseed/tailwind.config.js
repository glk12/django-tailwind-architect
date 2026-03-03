module.exports = {
  content: [
    // include all html templates and python files so Tailwind can see the
    // utility classes used by the Django templates when purging in production
    './templates/**/*.html',
    './**/templates/**/*.html',
    './**/views.py',
    './**/models.py',
    './**/urls.py',
    './**/forms.py',
    // if you have any other locations with Tailwind classes (e.g. JS), add
    // them here as well
  ],
  theme: {
    extend: {
      // the project gallery uses some non‑standard spacing values for
      // heights; make sure they exist in the generated stylesheet so they
      // won't be purged and the layout stays consistent between dev and
      // production
      spacing: {
        '59': '14.75rem',
        '67': '16.75rem',
        '76': '19rem',
      },
    },
  },
  // explicitly safelist a few utility classes that are generated
  // dynamically in templates so that they are always present even if the
  // content scanner misses them for some reason (e.g. during a CI/deploy
  // build). this makes the heights used by the project gallery available
  // in production and prevents the container from collapsing.
  safelist: [
    'h-59',
    'sm:h-67',
    'md:h-76',
  ],
  plugins: [require('daisyui')],
};

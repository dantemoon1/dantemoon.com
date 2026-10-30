export const site = {
  domain: 'dantemoon.com',
  name: 'Dante Moon',
  now: 'Data scientist at Optum. MCS student at UIUC. Living in Chicago.',
  description: 'Dante Moon: data scientist, builder, Chicago.',
};

// Hovering "Now" lays these out together on the display, like things pinned to a board.
// x, y (center) and w are fractions of the display; rotate is in degrees.
export const nowCollage = {
  name: 'Chicago · Optum · UIUC',
  credit: 'Home base, day job, school.',
  items: [
    { image: '/now/chicago-line.jpg', x: 0.37, y: 0.52, w: 0.66, rotate: -2 },
    { image: '/now/optum.png', x: 0.8, y: 0.26, w: 0.3, rotate: 4 },
    { image: '/now/illinois.png', x: 0.8, y: 0.7, w: 0.12, rotate: -6 },
  ],
};

export const projects = [
  {
    name: 'Aftershow',
    url: 'https://tryaftershow.com',
    host: 'tryaftershow.com',
    blurb: 'Feedback from every home showing, automatically.',
    image: '/shots/aftershow.jpg',
    crop: [0.07, 0.13, 0.42, 0.24],
  },
  {
    name: 'blockyourapps',
    url: 'https://blockyourapps.com',
    host: 'blockyourapps.com',
    blurb: 'Your AI agent blocks the apps that eat your day.',
    image: '/shots/blockyourapps.jpg',
    crop: [0.08, 0.33, 0.84, 0.28],
  },
  {
    name: 'Lofi New Tab',
    url: 'https://github.com/dantemoon1/lofi-newtab',
    host: 'github.com/dantemoon1',
    blurb: 'A calm new tab: lofi video, clock, pomodoro.',
    image: '/shots/lofi.jpg',
    crop: [0, 0, 1, 1],
  },
];

export const contact = [
  { label: 'email', value: 'dante@hey.com', url: 'mailto:dante@hey.com' },
  { label: 'github', value: 'dantemoon1', url: 'https://github.com/dantemoon1' },
  { label: 'linkedin', value: 'dantemoon', url: 'https://linkedin.com/in/dantemoon' },
];

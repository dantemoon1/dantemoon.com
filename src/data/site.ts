export const site = {
  name: 'Dante Moon',
  tagline: 'Data scientist and builder in Chicago.',
  email: 'dante@hey.com',
};

export type Station = {
  id: string;
  name: string;
  x: number;
  y: number;
  label: 'left' | 'right' | 'above' | 'below';
  terminal?: boolean;
  blurb: string;
  link?: { label: string; url: string };
};

export type Line = {
  id: string;
  name: string;
  color: string;
  // Track drawn from the Loop outward, in map coordinates.
  path: string;
  stations: Station[];
};

export const loop = {
  name: 'The Loop',
  blurb:
    "Hi, I'm Dante. I'm a data scientist at Optum, building ML models that read clinical text, and a Master of Computer Science student at UIUC. On the side I build products, mostly small, sometimes not. Pick a line to look around.",
};

export const lines: Line[] = [
  {
    id: 'build',
    name: 'Build Line',
    color: '#d6263b',
    path: 'M 545 330 L 545 250 L 445 150 L 445 70',
    stations: [
      {
        id: 'lofi',
        name: 'Lofi New Tab',
        x: 545,
        y: 268,
        label: 'right',
        blurb: 'A vibey new tab page. The first thing I made that people actually kept using.',
        link: { label: 'View on GitHub', url: 'https://github.com/dantemoon1/lofi-newtab' },
      },
      {
        id: 'aftershow',
        name: 'Aftershow',
        x: 495,
        y: 200,
        label: 'right',
        blurb:
          'Feedback from every home showing, automatically. Aftershow follows up with buyer agents after a showing and hands listing agents the answers. I build and run all of it.',
        link: { label: 'tryaftershow.com', url: 'https://tryaftershow.com' },
      },
      {
        id: 'blockyourapps',
        name: 'blockyourapps',
        x: 445,
        y: 70,
        label: 'right',
        terminal: true,
        blurb: 'My newest: an app blocker your AI agent can switch on for you, before Instagram eats the afternoon.',
        link: { label: 'blockyourapps.com', url: 'https://blockyourapps.com' },
      },
    ],
  },
  {
    id: 'work',
    name: 'Work Line',
    color: '#1c8ad8',
    path: 'M 520 395 L 390 395 L 290 495 L 130 495',
    stations: [
      {
        id: 'optum',
        name: 'Optum',
        x: 420,
        y: 395,
        label: 'above',
        blurb:
          'Data Scientist II on the clinical language team. Deep learning models that assign medical codes from clinical notes; I took one from 37 to 60 F1.',
      },
      {
        id: 'uiuc',
        name: 'UIUC',
        x: 130,
        y: 495,
        label: 'above',
        terminal: true,
        blurb: 'Master of Computer Science, the reason I moved to Chicago. Expected 2028.',
      },
    ],
  },
  {
    id: 'contact',
    name: 'Contact Line',
    color: '#1f9a4c',
    path: 'M 610 420 L 610 650',
    stations: [
      {
        id: 'email',
        name: 'Email',
        x: 610,
        y: 500,
        label: 'right',
        blurb: 'The fastest way to reach me.',
        link: { label: 'dante@hey.com', url: 'mailto:dante@hey.com' },
      },
      {
        id: 'github',
        name: 'GitHub',
        x: 610,
        y: 575,
        label: 'right',
        blurb: 'Side projects, old and new.',
        link: { label: 'github.com/dantemoon1', url: 'https://github.com/dantemoon1' },
      },
      {
        id: 'linkedin',
        name: 'LinkedIn',
        x: 610,
        y: 650,
        label: 'right',
        terminal: true,
        blurb: 'The résumé version.',
        link: { label: 'linkedin.com/in/dantemoon', url: 'https://linkedin.com/in/dantemoon' },
      },
    ],
  },
];

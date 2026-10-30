# dantemoon.com

My personal site: a receipt printed on e-ink.

On desktop, the receipt sits next to a little e-ink display. Hover a project and the display does a partial refresh to show a dithered screenshot of it. On phones, the screenshots are printed inline on the receipt.

Built with [Astro](https://astro.build) and hosted on Cloudflare Workers.

## Editing

All the words, projects and images are in `src/data/site.ts`. Screenshots live in `public/shots/`, the "Now" collage in `public/now/`. Images are dithered in the browser, so drop in a normal screenshot.

## Running it

```sh
npm install
npm run dev      # http://localhost:4321
npm run deploy   # build and publish to dantemoon.com
```

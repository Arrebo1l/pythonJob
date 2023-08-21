# With npm
npm i @popperjs/core

# With Yarn
yarn add @popperjs/core

<!-- Development version -->
<script src="https://unpkg.com/@popperjs/core@2/dist/umd/popper.js"></script>

<!-- Production version -->
<script src="https://unpkg.com/@popperjs/core@2"></script>

<!DOCTYPE html>
<title>Popper example</title>

<style>
  #tooltip {
    background-color: #333;
    color: white;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 13px;
  }
</style>

<button id="button" aria-describedby="tooltip">I'm a button</button>
<div id="tooltip" role="tooltip">I'm a tooltip</div>

<script src="https://unpkg.com/@popperjs/core@2"></script>
<script>
  const button = document.querySelector('#button');
  const tooltip = document.querySelector('#tooltip');

  // Pass the button, the tooltip, and some options, and Popper will do the
  // magic positioning for you:
  Popper.createPopper(button, tooltip, {
    placement: 'right',
  });
</script>

import { createPopper } from '@popperjs/core';

const button = document.querySelector('#button');
const tooltip = document.querySelector('#tooltip');

// Pass the button, the tooltip, and some options, and Popper will do the
// magic positioning for you:
createPopper(button, tooltip, {
  placement: 'right',
});

import { createPopper } from '@popperjs/core/lib/popper-lite.js';

import { createPopper } from '@popperjs/core/lib/popper-lite.js';
import preventOverflow from '@popperjs/core/lib/modifiers/preventOverflow.js';
import flip from '@popperjs/core/lib/modifiers/flip.js';

const button = document.querySelector('#button');
const tooltip = document.querySelector('#tooltip');

createPopper(button, tooltip, {
  modifiers: [preventOverflow, flip],
});
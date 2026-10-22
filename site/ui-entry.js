import '@santi020k/lumen-elements/styles.css';
import { defineLumenCard } from '@santi020k/lumen-elements/components/card';
import { defineLumenBadge } from '@santi020k/lumen-elements/components/badge';
import { defineLumenButton } from '@santi020k/lumen-elements/components/button';

// Register only the primitives this static site uses, not the full catalog.
defineLumenCard();
defineLumenBadge();
defineLumenButton();

// Native controls remain readable in the unenhanced document. Upgrade before
// attaching application listeners so focus, state and click handlers stay on one node.
document.querySelectorAll('.filter-button, .search-clear, .copy-handle').forEach(button => {
  const control = document.createElement('lumen-button');
  for (const { name, value } of button.attributes) control.setAttribute(name, value);
  control.setAttribute('variant', 'outline');
  control.append(...button.childNodes);
  button.replaceWith(control);
});

await import('./site.js');

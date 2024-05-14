document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.read-more').forEach(item => {
        item.addEventListener('click', event => {
            event.preventDefault();
            const fullText = item.getAttribute('data-full-text');
            item.parentElement.innerHTML = fullText;
        });
    });
});
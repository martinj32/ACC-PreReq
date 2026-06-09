// ACC Quiz Component
// Uses document$.subscribe() so it re-runs on every Material instant-nav page transition.

document$.subscribe(function () {
  document.querySelectorAll(".quiz-block:not([data-initialized])").forEach(function (block) {
    block.setAttribute("data-initialized", "true");

    var options  = block.querySelectorAll(".quiz-options li");
    var feedback = block.querySelector(".quiz-feedback");
    var isMulti  = block.hasAttribute("data-multi");

    options.forEach(function (option) {
      option.addEventListener("click", function () {
        var isCorrect = option.dataset.correct === "true";

        if (!isMulti) {
          // Single-answer: clear all previous marks before applying new one
          options.forEach(function (o) {
            o.classList.remove("quiz-correct", "quiz-incorrect");
          });
        }

        option.classList.remove("quiz-correct", "quiz-incorrect");
        option.classList.add(isCorrect ? "quiz-correct" : "quiz-incorrect");

        if (feedback) {
          if (isCorrect) {
            feedback.textContent  = "✓ Correct!";
            feedback.className    = "quiz-feedback quiz-feedback-correct";
          } else {
            feedback.textContent  = "✗ Not quite — try again.";
            feedback.className    = "quiz-feedback quiz-feedback-incorrect";
          }
        }
      });
    });
  });
});

const myHeading = document.querySelector("h1");
const myImage = document.querySelector("img");
const myButton = document.querySelector("button");

// Change heading text
myHeading.textContent = "Hello world!";

// Image toggle
myImage.addEventListener("click", () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "Look_at_me_go.png") {
    myImage.setAttribute("src", "Boo.png");
  } else {
    myImage.setAttribute("src", "Look_at_me_go.png");
  }
});

// Name function
function setUserName() {
  const myName = prompt("Please enter your name.");
  localStorage.setItem("name", myName);
  myHeading.textContent = `Mozilla is cool, ${myName}`;
}

// Load stored name
if (!localStorage.getItem("name")) {
  setUserName();
} else {
  const storedName = localStorage.getItem("name");
  myHeading.textContent = `Mozilla is cool, ${storedName}`;
}

// Button click
myButton.addEventListener("click", () => {
  setUserName();
});
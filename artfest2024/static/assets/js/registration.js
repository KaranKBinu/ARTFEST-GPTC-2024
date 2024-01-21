const nameInput = document.getElementById("student_name");
const emailInput = document.getElementById("student_email");
const phoneInput = document.getElementById("student_phone");
const admnNoInput = document.getElementById("student_admn_no");
const submitButton = document.getElementById("submit_button");
const passwordInput = document.getElementById("student_password");
const confirmPasswordInput = document.getElementById("confirm_password");

// Cache result elements
const resName = document.getElementById("res_name");
const resEmail = document.getElementById("res_email");
const resPhone = document.getElementById("res_phone");
const resAdmnNo = document.getElementById("res1");
const resPwd = document.getElementById("res_pwd");
const resCpwd = document.getElementById("res_cpwd");

// Event listeners
nameInput.addEventListener("input", checkName);
emailInput.addEventListener("input", checkEmail);
phoneInput.addEventListener("input", checkPhone);
admnNoInput.addEventListener("input", checkAdmnNo);
passwordInput.addEventListener("input", checkPassword);
confirmPasswordInput.addEventListener("input", checkConfirmPassword);

function checkValidity() {
  const isPasswordValid = passwordInput.value.length >= 6;
  const isConfirmPasswordValid = confirmPasswordInput.value === passwordInput.value;
  const isNameValid = nameInput.value.length >= 3;
  const isEmailValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value);
  const isPhoneValid = !isNaN(parseInt(phoneInput.value)) && phoneInput.value.toString().length === 10;
  const isAdmnNoValid = !isNaN(parseInt(admnNoInput.value)) && admnNoInput.value.toString().length === 4;

  submitButton.disabled = !(
    isNameValid &&
    isEmailValid &&
    isPhoneValid &&
    isAdmnNoValid &&
    isPasswordValid &&
    isConfirmPasswordValid
  );
  submitButton.style.cursor = submitButton.disabled ? "not-allowed" : "pointer";
  submitButton.style.backgroundColor = submitButton.disabled ? "gray" : "#00bdfe";
}

function checkName() {
  checkValidity();
  const isNameValid = nameInput.value.length >= 3;
  resName.innerHTML = isNameValid ? "" : "Please fill properly";
  nameInput.style.border = isNameValid
    ? "2px solid rgb(20, 245, 2)"
    : "2px solid red";
}

function checkEmail() {
  checkValidity();
  const isEmailValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value);
  resEmail.innerHTML = isEmailValid ? "" : "Invalid email address";
  emailInput.style.border = isEmailValid
    ? "2px solid rgb(20, 245, 2)"
    : "2px solid red";
}

function checkPhone() {
  checkValidity();
  const isPhoneValid =
    !isNaN(parseInt(phoneInput.value)) &&
    phoneInput.value.toString().length === 10;
  resPhone.innerHTML = isPhoneValid
    ? ""
    : "Phone Number Must be 10 digits & Numeric.";
  phoneInput.style.border = isPhoneValid
    ? "2px solid rgb(20, 245, 2)"
    : "2px solid red";
}

function checkAdmnNo() {
  checkValidity();
  const a = isNaN(parseInt(admnNoInput.value));
  const b = admnNoInput.value.toString();

  const isAdmnNoValid = !a && b.length === 4;
  resAdmnNo.innerHTML = isAdmnNoValid
    ? ""
    : "Admission number should have 4 digits.";
  admnNoInput.style.border = isAdmnNoValid
    ? "2px solid rgb(20, 245, 2)"
    : "2px solid red";
}

function checkPassword() {
  checkValidity();
  const isPasswordValid = passwordInput.value.length >= 6;
  resPwd.innerHTML = isPasswordValid
    ? ""
    : "Password should be at least 6 characters long";
  passwordInput.style.border = isPasswordValid
    ? "2px solid rgb(20, 245, 2)"
    : "2px solid red";
}

function checkConfirmPassword() {
  checkValidity();
  const isConfirmPasswordValid =
    confirmPasswordInput.value === passwordInput.value;
  resCpwd.innerHTML = isConfirmPasswordValid ? "" : "Passwords do not match";
  confirmPasswordInput.style.border = isConfirmPasswordValid
    ? "2px solid rgb(20, 245, 2)"
    : "2px solid red";
}

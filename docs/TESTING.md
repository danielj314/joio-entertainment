# Testing

The Joio Entertainment website has been tested using the following methods:
- [Code Validation](#code-validation)
    - [W3C HTML Validator](#w3c-html-validator) 
    - [W3C CSS Validator](#w3c-css-validator)
    - [JSHINT Javascript Code Quality Tool](#jshint-javascript-code-quality-tool)
    - [Python Validation using Gitpod](python-validation-using-gitpod)
- [Accessibility](#accessibility)
    - [Colour Contrast](#colour-contrast)
    - [Wave Webaim Accessibility Checker](#wave-webaim-accessibility-checker)
- [Lighthouse](#lighthouse)
- [Responsiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Testing User Stories](#testing-user-stories)
    - [First Time User](#first-time-user)
    - [Returning User](#returning-user)
    - [Business Owner](#business-owner)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [Peer Review](#peer-review)
- [Bugs](#bugs)
    - [Resolved](#resolved)
    - [Unresolved](#unresolved)

# Code Validation

## W3C HTML Validator

The Joio Entertainmet website pages passed all tests using the W3C HTML Validator tool

Links to images of tests:
<h2 align="center"><img src="TESTING/html-validation/about.jpg"></h2>

<h2 align="center"><img src="TESTING/html-validation/bag.jpg"></h2>

<h2 align="center"><img src="TESTING/html-validation/checkout.jpg"></h2>

<h2 align="center"><img src="TESTING/html-validation/contact.jpg"></h2>

<h2 align="center"><img src="TESTING/html-validation/home.jpg"></h2>

<h2 align="center"><img src="TESTING/html-validation/login.jpg"></h2>

<h2 align="center"><img src="TESTING/html-validation/logout.jpg"></h2>

<h2 align="center"><img src="TESTING/html-validation/prod-details.jpg"></h2>

<h2 align="center"><img src="TESTING/html-validation/products-add.jpg"></h2>

<h2 align="center"><img src="TESTING/html-validation/products.jpg"></h2>

<h2 align="center"><img src="TESTING/html-validation/profile.jpg"></h2>

<h2 align="center"><img src="TESTING/html-validation/signup.jpg"></h2>

When first tested, every page had a Warning notification for an unnecessary attribute. This was removed and following that, all pages passed the html checks.

<h2 align="center"><img src="TESTING/html-validation/success.jpg"></h2>

## W3C CSS Validator

The Joio website passed all tests using the W3C CSS Validator tool

base.css:
<h2 align="center"><img src="TESTING/css-validation/base-css.jpg"></h2>

checkout.css:
<h2 align="center"><img src="TESTING/css-validation/checkout-css.jpg"></h2>


## JSHINT Javascript Code Quality Tool

The Joio website passed all tests using the JSHint Validator tool

stripe_elements.js:

<h2 align="center"><img src="TESTING/js-validation/stripe-elements1.jpg"></h2>

<h2 align="center"><img src="TESTING/js-validation/stripe-elements2.jpg"></h2>

quantity_input_script.html:

<h2 align="center"><img src="TESTING/js-validation/qty-input-scripts.jpg"></h2>

* There were warnings highlighted by JSHint related to using a template literal syntax. However, as the code performs correctly, it was decided this was not a concern.
* There are undefined variables that are being picked up -stripe, which is defined in another script -the $ signs which doesnt seem logical as they are not variables.


## Python Validation using Gitpod

* I have checked all Python documents using command "python3 -m flake8" in the terminal to ensure they are compliant.

* All issues were rectified, except for code I have not written in Django settings.


# Stem & Leaf - Testing Documentation

**image here**

I recently had the opportunity to sit the ISTQB foundation level and used my new knowledge to follow the 7 testing principles:

1. Testing shows the presence, not absence, of defects
2. Exhaustive testing is impossible
3. Early testing saves time and money
4. Defects cluster together 
5. Be aware of the pesticide paradox 
6. Testing is context dependent
7. Absence-of-errors is a fallacy

In considering the above, the below is the documentation of my testing process. This will be a living document and I hope to include more robust and automated testing frameworks in the future.

## Contents
- [Validation Testing](#validation-testing)
  * [CSS](#css)
  * [JavaScript](#javascript)
  * [Python](#python)
- [Visual (UI) Testing: Cross Browser and Cross Device Testing](#visual--ui--testing--cross-browser-and-cross-device-testing)
- [Lighthouse](#lighthouse)
    + [Desktop Results](#desktop-results)
    + [Mobile Results](#mobile-results)
  * [Wave](#wave)
- [Automated Testing](#automatic-testing)
- [Manual Testing](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
- [Outstanding Defects](#outstanding-defects)
- [Defects of Note](#defects-of-note)

## Validation Testing
[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilises Django templating language within the HTML, I have checked the HTML by inspecting the page source and then running this through the validator. You can click each page to see the corresponding screenshot evidence.

| Page | Result |
| :--- | :--- |
| [Home Page](#) | Pass |
| [Service Page](#) | Pass |
| [Cat Profile](#) | Pass |
| [Cat Detail](#)| Pass |
| [Edit Cat Page](#) | Pass |
| [Delete Cat Page](#) | Pass |
| [Booking Page](#) | Fail |
| [My Bookings](#) | Pass |
| [Checkout Page](#) | Pass |
| [Checkout Success Page](#) | Pass |
| [Error 404](#) | Pass |

**Please note:**
- XX

### CSS

[W3C](https://validator.w3.org/) was used to validate the CSS. 

| File | Result | 
| :--- | :--- |
| [static/base.css](#) | Pass |
| [checkout/static/checkout.css](#) | Pass |

### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

| File | Result |
| :--- | :--- |
| [checkout/static/stripe_elements.js](#) | Pass |

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python. I have also installed [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration) in my IDE to enable me to check my code meets PEP8 guidelines during development.

| File | Result |
| :--- | :--- |
| [custom_storages.py](#)  | Pass | 
| **PURRFECT SITTERS** |
| [purrfect_sitters/urls.py](#) | Pass |  
| **HOME** |
| [home/views.py](#) | Pass | 
| [home/urls.py](#) | Pass | 
| **SERVICES** |
| [service/models.py](#) | Pass | 
| [service/views.py](#) | Pass | 
| [service/admin.py](#) | Pass | 
| [vservice/urls.py](#) | Pass |  
| **CAT** |
| [cat/models.py](#) | Pass | 
| [cat/views.py](#) | Pass | 
| [cat/urls.py](#) | Pass | 
| [cat/admin.py](#) | Pass | 
| [cat/forms.py](#) | Pass | 
| **BOOKING** |
| [booking/models.py](#) | Pass | 
| [booking/views.py](#) | Pass | 
| [booking/urls.py](#) | Pass | 
| [booking/admin.py](#) | Pass | 
| [booking/forms.py](#) | Pass | 

## Visual (UI) Testing: Cross Browser and Cross Device Testing
- The below combination of devices, browsers, and operating system were used to test the website. A range of viewport sizes were checked to see if users would have the same experience across multiple devices and browsers. Priority was given to mobile devices and tablets. 

| **TOOL / Device**           | **BROWSER**      | **OS**  | **SCREEN WIDTH** | Passed 
|-----------------------------|------------------|---------|------------------|---------
| dev tools: Galaxy Fold      | Chrome           | android | 280 x 653 px     |Yes
| dev tools: iPhone SE        | safari           | iOs     | 375 x 667 px     |Yes
| dev tools: Samsung S8+      | Chrome           | android | 360 x 740 px     |Yes
| real phone: Pixel 6         | Chrome           | android | 393 x 851 px     |Yes
| real phone: iPhone 14 Pro   | safari           | iOs     | 390 x 844 px     |Yes
| browserstack: Nexus 7       | Firefox          | android | 960 x 600 px     |Yes
| real tablet: Pixel Tablet   | Chrome           | android | 834 x 1075 px    |Yes
| real laptop: Macbook Pro    | Firefox & Chrome | iOs     | 1400 x 766 px    |Yes
| broswerstack                | Firefox          | iOs     | 1440 x 672 px    |Yes
| browserstack                | Edge 113         | windows | 1440 x 672 px    |Yes

## Lighthouse

For the performance, accessibility, best practices and SEO of the site for mobile and desktop, [Page Speed](https://pagespeed.web.dev/) and the major pages were passed through the validation. 

#### Desktop Results

| Page | Result |
| :--- | :--- |
| Home Page | # |
| Service Page | # |
| Cat Profile | # |
| Booking | # |
| Checkout | # |

- Desktop performed well on all major pages of the site with minimal improvements needed.

#### Mobile Results

| Page | Result |
| :--- | :--- |
| Home Page | # |
| Service Page | # |
| Cat Profile | #|
| Booking | # |
| Checkout | # |

- XX
- XX

### Wave

WAVE(Web Accessibility Evaluation Tool) allows developers to create content that is more accessible to users with disabilities. It does this by identifying accessibility and WGAC errors. The following pages were tested:

| Page | Errors |
| :--- | :--- |
| Home Page | 1 error|
| Service Page | No errors |
| Cat Profile | No errors |
| Cat Detail| No errors |
| Add Cat | No errors |
| Edit Cat| No errors |
| Booking | No errors |
| Checkout | No errors |

- XX

## Automated Testing
- Manual testing was done due to time constraints.
- Testing of each app views will be done using Django unittest module in the next iteration.
- I am keen to investigate HTTP-level request handling, form validation and processing and template rendering using automated tests.
- This is a great area of interest to me, and I was disappointed to not have been able to implement these in time.

## Manual Testing

### Testing User Stories
- Each completed user story on the [sprint backlog](#) was tested against the acceptance criteria, see the corresponding screenshots as evidence.
- This included reviewing each feature to check the usability, visual design and performance.

(user stor ytesting table goes here)

## Outstanding Defects
- XX

## Defects of Note
- XX 
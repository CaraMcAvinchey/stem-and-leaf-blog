# Stem & Leaf - Testing Documentation

![Screenshot 2023-06-08 at 20 40 58](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/411b58bf-5403-4186-b546-ea12e0b51a07)

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
| [Home Page](documentation/testing/html/home.png) | Pass |
| [Plant Detail](documentation/testing/html/plant_detail.png) | Pass |
| [Edit Comment](documentation/testing/html/edit_comment.png) | Pass |
| [Sign up](documentation/testing/html/signup.png)| Pass |
| [Login](documentation/testing/html/login.png) | Pass |
| [Logout](documentation/testing/html/logout.png) | Pass |
| [Error 404](documentation/testing/html/error404.png) | Pass |

### CSS

[W3C](https://validator.w3.org/) was used to validate the CSS. 

| File | Result | 
| :--- | :--- |
| [static/css/style.css](documentation/testing/css.png) | Pass |

### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

| File | Result |
| :--- | :--- |
| [static/js/script.js](documentation/testing/js.png) | Pass |

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python. I have also installed [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration) in my IDE to enable me to check my code meets PEP8 guidelines during development.

| File | Result |
| :--- | :--- |
| **STEAMAND LEAF** |
| [stemandleaf/urls.py](documentation/testing/python/project_urls.png) | Pass |  
| **BLOG** |
| [blog/views.py](documentation/testing/python/views.png) | Pass | 
| [blog/models.py](documentation/testing/python/models.png) | Pass | 
| [blog/forms.py](documentation/testing/python/forms.png) | Pass |
| [blog/urls.py](documentation/testing/python/app_urls.png) | Pass | 
| [blog/admin.py](documentation/testing/python/admin.png) | Pass | 

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
| Home Page | ![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/ebca9a5b-1544-4d9d-99ce-8974f8d49df7) |
| Plant Detail | ![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/7a0b842a-d9bb-4043-a241-f0b1463abfd1) |
| Edit Comment | ![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/a63fbfb9-2540-4388-a02f-a265278c87f0) |
| Delete Comment | ![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/247ab8df-7a5f-49dc-a9b7-d08964dfc462) |
| Sign up |![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/8f2091da-ae4c-474f-8bd6-e065942f9c0e) |
| Login | ![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/f0aa109a-8830-43bd-8812-5177f9ccc342) |

- Desktop performed well on all major pages of the site with minimal improvements needed.

#### Mobile Results

| Page | Result |
| :--- | :--- |
| Home Page | ![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/20ada406-0037-4620-a467-d83f4be7195e) |
| Plant Detail | ![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/d5c2a909-d6a9-407a-935a-7b00ed9d1ac8) |
| Edit Comment | ![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/c56076ee-b356-446d-bdd6-31fa29db8c2c) |
| Delete Comment | ![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/f1ceec54-84de-4805-9a03-76e3cf66c422) |
| Sign up | ![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/b486a109-ccfe-433d-be6b-befec7fa67d3) |
| Login | ![image](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/b9781ec2-66a3-4bc5-97e3-9528863aeeac) |

- Mobile performance can improve, where performance was slower due to first contentful paint and largest contentful paint metrics.
- This is a result of render-blocking resources mostly from Bootstrap and Cloudinary which requires further investigation to resolve.
- More investigation needed to see if defer/async is a better option including code minification and seeing if moving the scripts out of the head would in base.html would affect the performance or not.

### Wave

WAVE(Web Accessibility Evaluation Tool) allows developers to create content that is more accessible to users with disabilities. It does this by identifying accessibility and WGAC errors. The following pages were tested:

| Page | Result |
| :--- | :--- |
| [Home](documentation/testing/wave-home.png) | 0 errors |
| [Plant Detail](documentation/testing/wave-home.png) | 0 errors  |

- The contrast errors found were tested and the dark green colour adjusted and retested:

<img width="731" alt="210070268-17725578-409a-4278-a99e-60e844ddb1b8" src="https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/adf13c93-8cbe-49ed-83f0-e4624f91c8a5">

## Automated Testing
- Manual testing was done due to time constraints.
- Testing of each app views will be done using Django unittest module in the next iteration.
- I am keen to investigate HTTP-level request handling, form validation and processing and template rendering using automated tests.
- This is a great area of interest to me, and I was disappointed to not have been able to implement these in time.

## Manual Testing

### Testing User Stories
- Each completed user story on the [sprint backlog](https://github.com/users/CaraMcAvinchey/projects/4) was tested against the acceptance criteria, see the corresponding screenshots as evidence.
- This included reviewing each feature to check the usability, visual design and performance.

|  | USER STORY | TEST CASE | RESULT |
|---|---|---|---|
|  | As a **site user**, I can **register an account** so that **I can interact with blog posts**. |  | PASS |
|  | As a **site user**, I can **view a list of posts** so that **I can select one to read**. |  | PASS |
|  | As a **site user**, I can **click on a post** so that **I can read the full article** and find out more about plant care. |  | PASS |
|  | As a **site user**, I can **view the number of likes on each post** so that **I can see which plants are popular.** |  | PASS |
|  | As a **site user**, I can **like a post** so that **I can engage with the blog content**. |  | PASS |
|  | As a **site user**, I can **view comments on a post** so that **I can read other user feedback**. |  | PASS |
|  | As a **site user**, I can **leave comments on a post** so that **I can share my own feedback.** |  | PASS |
|  | As a **site user**, I can **edit and delete my comments on a post** so that **I can customise or remove my thoughts** if required. |  | PASS |
|  | As a **site user**, I can **return to the home page** of the blog if there is an error so that **I don’t get lost on the website**. |  | PASS |
|  | In order to **create and control the content for the blog** as an **admin user**, **I can access the admin panel using admin login details.** |  | PASS |
|  | In order to **finish writing or publish content later** as an **admin user**, **I can create draft posts.** |  | PASS |
|  | In order to **manage the blog content** as an **admin user**, **I can create, read, update and delete posts** using the admin panel. |  | PASS |
|  | In order to **maintain a positive community atmosphere** as an **admin user**, **I can approve/disapprove comments.** |  | PASS |

## Outstanding Defects
- There are no outstanding defects.

## Defects of Note
- The user story for [OPEN A POST](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/issues/8) had multiple challenges including styling issues with the summary card, the likes/comments area and rendering of the plant detail model information. 
 - The styling challenges were solved using margins and restructuring of some div elements.
 - The comments/likes area required some guidance from my mentor to establish what the user sees when logged in, logged out and restructured the template from there.

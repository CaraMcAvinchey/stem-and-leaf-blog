# STEM & LEAF - A PLANT CARE SPACE FOR BEGINNERS

## Author
Cara McAvinchey 

## Project Overview
*  The Stem & Leaf blog is a place for plant care beginners to visit and learn about how to take care of their plants. Each blog post is dedicated to a popular house plant, with a short write up and tips on how to maintain it. 

You can view the deployed website [here](https://stem-and-leaf-blog.herokuapp.com/)

<img width="1028" alt="image" src="https://user-images.githubusercontent.com/97494262/209436822-8a40360c-cb65-4abf-bd98-5869aec18d12.png">

## UX

### Project Goal
* The aim of the project is to provide easily digestible information about popular house plants for beginners and to allow for conversation and sharing of experiences in taking care of them.

### User Stories
* For sight users:
   1. As a **site user**, I can **register an account** so that **I can interact with blog posts**.
   2. As a **site user**, I can **view a list of posts** so that **I can select one to read**.
   3. As a **site user**, I can **click on a post** so that **I can read the full article** and find out more about plant care**.**
   4. As a **site user**, I can **view the number of likes on each post** so that **I can see which plants are popular.**
   5. As a **site user**, I can **like a post** so that **I can engage with the blog content**.
   6. As a **site user**, I can **view comments on a post** so that **I can read other user feedback**.
   7. As a **site user**, I can **leave comments on a post** so that **I can share my own feedback.**
   8. As a **site user**, I can **edit and delete my comments on a post** so that **I can customise or remove my thoughts** if required.
   9. As a **site user**, I can **use the search bar** so that **I can find plants I am looking for**.
   10. As a **site user**, I can **save my favourite plant posts** so that **I have all my houseplants I care for in the same place.**
   11. As a **site user**, I can **rate blog posts on a scale of 1-5** so that **I can give feedback about which content I enjoy most**.
   12. As a **site user**, I can **return to the home page** of the blog if there is an error so that **I don’t get lost on the website**.

* For admin users:
    13. In order to **create and control the content for the blog** as an **admin user**, **I can access the admin panel using admin login details.**
    14. In order to **finish writing or publish content later** as an **admin user**, **I can create draft posts.**
    15. In order to **manage the blog content** as an **admin user**, **I can create, read, update and delete posts** using the admin panel.
    16. In order to **maintain a positive commnity atmosphere** as an **admin user**, **I can approve/disapprove comments.**  
 
## DESIGN CHOICES

### Colors
<img width="538" alt="image" src="https://user-images.githubusercontent.com/97494262/209437405-63db90ed-fd86-4285-8a19-002c73a2d1a7.png">
 
- The natural color palette links to the theme of plants and plant care. 
- The headings, icons and body text are darker to ensure clear contrast and readability for the user across the site.
- The green header and footer ensures clear contrast and delineation between sections.

### Typography
<img width="896" alt="image" src="https://user-images.githubusercontent.com/97494262/209437426-7c754f60-85b0-4d60-9f17-04caedb8f635.png">

- The font combination was chosen using guidance from Mai Knoblovits [here](https://artisanthemes.io/great-google-font-combinations-ready-use/)
- The logo and headings use Amatic SC with a fallback of cursive and the body text uses Roboto Condensed with a fallback of san-serif.
- The choice of fonts were selected and installed using [Google Fonts](https://fonts.google.com/).

### Images/Icons
<img width="351" alt="image" src="https://user-images.githubusercontent.com/97494262/209437645-30a1ff77-27cb-4eea-a342-6aa1592cb81d.png">

- The icons were chosen to provide clear understanding of each plant and its care requirements.
- Each summary card has the same information structure with all icons standard throughout the site.

### Animations
- The navbar, social icons and buttons across the site have a subtle grow effect when hovered over by the user.
- All links have a color change and underlined effect when hovered for clear distinction from the body text.

### Responsiveness
- The website was designed mobile-first using flexbox to ensure responsiveness throughout the website.
- The standard grid from Bootstrap was used to achieve this.

## WIREFRAMES

### Post List
- The post list page was designed using cards to show a quick summary of each plant.
- The user can click and find out more about a plant that interests them.
<img width="636" alt="image" src="https://user-images.githubusercontent.com/97494262/209437372-83b2bc1e-68a0-4a75-8e86-d78b69df4a7d.png">

### Post Detail
- Each blog post provides detail about the plant and a list of instructions to care for it. 
- The registered user can also comment and like the post if desired.
<img width="611" alt="image" src="https://user-images.githubusercontent.com/97494262/209437385-b8be9fe9-bbbb-4110-a9af-e0f5239f3cc9.png">

## FEATURES/STRUCTURE

### Welcome Area
- XX
- XX

### Game Score Area
- XX

### Game Controls 
- XX
- XX

### Game Rules
- XX

### JavaScript Enable Message
- XX

### Footer
- XX
- XX

### Error 404
- XX
- XX

### Features for Future Development
- XX
- XX
- XX

## DATA MODEL
- XX
(data tables)

[x] C -
[x] R -
[x] U -
[x] D -

## TESTING

### Validation Testing
- HTML
   - No errors were returned when passing through the official [HTML validator]("https://validator.w3.org/nu/?doc=https%3A%2F%2Fcaramcavinchey.github.io%2Frock-paper-scissors%2F").

- CSS
   - No errors were found when passing through the [CSS validator]("https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcaramcavinchey.github.io%2Frock-paper-scissors%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en").

### Cross Browser and Cross Device Testing
- The below combination of devices, browsers, and operating system were used to test the website. A range of viewport sizes were checked to see if users would have the same experience across multiple devices and browsers.

| **TOOL / Device**           | **BROWSER**      | **OS**  | **SCREEN WIDTH** |
|-----------------------------|------------------|---------|------------------|
| dev tools: Galaxy Fold      | Chrome           | android | 280 x 653 px     |
| dev tools: iPhone SE        | safari           | iOs     | 375 x 667 px     |
| dev tools: Pixel 2          | Chrome           | android | 411 x 731        |
| real phone: iPhone XR       | safari           | iOs     | 414 x 896 px     |
| browserstack: Nexus 7       | Firefox          | android | 960 x 600 px     |
| browserstack: iPhone 13 Pro | safari           | iOs     | 390px × 844px    |
| real tablet: iPad Pro 11    | Chrome           | iOs     | 834 x 1075 px    |
| real laptop: Macbook Pro    | Firefox & Chrome | iOs     | 1400 x 766 px    |
| broswerstack                | Firefox          | iOs     | 1440 x 672 px    |
| browserstack                | Edge 99          | windows | 1440 x 672 px    |

### Manual Testing
- You can view manual testing of the website [here](https://docs.google.com/spreadsheets/d/123Pia98Ms_Fe6at0hPnAWhcNrmeVc4X2RLYmD7VsqX4/edit?usp=sharing).

### Automatic Testing

### Outstanding Defects
- XX

### Defects of Note
- XX

## ACCESSIBILITY

### Lighthouse Audit
- XX

### Keyboard Navigation
- XX

## TECHNOLOGIES USED
- Gitpod
- Github
- Django
- Bootstrap
- Cloudinary
- Summernote
- Crispy Forms
- Heroku
- Balsamiq
- Fontawesome

## DEPLOYMENT
* Step 1: Create a new app in Heroku, choose a unique name and region.
* Step 2: Login to ElephantSQL, access the dashboard and create a new instance (input a name, select a region).
* Step 3: Return to dashboard, copy the database URL:
<img width="1074" alt="image" src="https://user-images.githubusercontent.com/97494262/209531384-85d95cc3-a381-4c3c-b56f-215238e0daf8.png">
* Step 4: Create env.py file (ensure it is included in .gitignore file) and add environment the below variables. Paste the URL from above:
<img width="372" alt="image" src="https://user-images.githubusercontent.com/97494262/209531222-599282ee-2c54-490f-b543-1f09e5255490.png">
* Step 5: Include a secret key in the variables:
<img width="953" alt="Screenshot 2022-12-26 at 11 25 13" src="https://user-images.githubusercontent.com/97494262/209531979-9ba177cc-3e44-48a7-80dc-884d06932f54.png">
* Step 6: Include the below code to settings.py file:
<img width="301" alt="image" src="https://user-images.githubusercontent.com/97494262/209532128-acaa1e29-edea-45c3-93ce-2caaf0f71862.png">
* Step 7: Link the database in settings.py and migrate then push to GitHub:
<img width="303" alt="image" src="https://user-images.githubusercontent.com/97494262/209532393-5283592f-5caf-4e81-b3fd-9d20bd62b111.png">
* Step 8: In Heroku, add three config vars:
<img width="243" alt="image" src="https://user-images.githubusercontent.com/97494262/209532605-04bff00b-951f-4084-9ad5-6eff111ac6bf.png">
<img width="350" alt="image" src="https://user-images.githubusercontent.com/97494262/209532533-e9b3d879-a40a-4335-a56b-3c0e5c370a8a.png">
* Step 9: Login to Cloudinary, copy the API Environmental variable to dashboard and add to env.py (see screenshot above) & to Heroku config vars:
<img width="571" alt="image" src="https://user-images.githubusercontent.com/97494262/209533286-4a79143c-6568-4055-99fc-76dd5821a02b.png">
* Step 10: Add cloudinary to installed apps in settings.py, add static/media file settings:
<img width="407" alt="image" src="https://user-images.githubusercontent.com/97494262/209533445-8f6670c5-490b-4294-95cf-febaaaed2ab2.png">
<img width="853" alt="image" src="https://user-images.githubusercontent.com/97494262/209533629-ab3fb31b-f096-4305-996e-970e4c950a3f.png">
* Step 11: Add template directories in settings.py, add Heroku host name to allowed hosts and add directory files:
<img width="746" alt="image" src="https://user-images.githubusercontent.com/97494262/209533879-b8284837-e7a1-4315-83e6-9b88d2125882.png">
<img width="501" alt="image" src="https://user-images.githubusercontent.com/97494262/209534100-46723f98-7bd6-40ed-91c1-5226ad6e950d.png">
<img width="313" alt="image" src="https://user-images.githubusercontent.com/97494262/209534271-772afed4-f299-45dc-b72d-d0843b7ad189.png">
* Step 12: Create a Procfile, then commit and push to GitHub:
<img width="504" alt="image" src="https://user-images.githubusercontent.com/97494262/209534389-5b0cdd3c-54f7-44e8-8a21-99068431365a.png">
* Step 13: Connect GitHub account in Heroku, connect and deploy branch. Open app and check:
<img width="421" alt="image" src="https://user-images.githubusercontent.com/97494262/209534580-c03fa4fd-8e52-487b-8ecc-23563fd30327.png">

## CREDITS
- The Code Institute 'I Think, Therefore I Blog' walkthrough project assisted and guided in the setup and basic structure of this project.
- The Stockbook Project by Massimo Ranalli assisted with the setup of the edit/delete functions for comments.
- Code Institute Student Template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template).

### Media
- The fonts were chosen with guidance from an article written by Mai Knoblovits [here](https://artisanthemes.io/great-google-font-combinations-ready-use/).
- The colors for the website was generated using [Color Space]([https://coolors.co/image-picker](https://mycolor.space/?hex=%2333C883&sub=1)).
- The plant images were sourced using [Pexels](https://www.pexels.com) and [Pixabay](https://pixabay.com/).
- The icons for the favicon, footer, about page and location headings were taken from [Font Awesome](https://fontawesome.com/).
- The favicon image was converted using [Favicon.io](https://favicon.io/).

## ACKNOWLEDGEMENTS
- Thank you to my mentor for continuous helpful feedback and support throughout the project.
- The tutors at Code Institute for their patience and support.
- The Code Institute Slack community for tips and guidance.

[Back to the beginning](#table-of-contents)

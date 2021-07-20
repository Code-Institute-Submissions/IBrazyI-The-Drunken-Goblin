# The Drunken Goblin (Milestone Project 3)

![The Drunken Goblin](/static/images/responsive.jpg)

[Visit My Site Here](https://the-drunken-goblin.herokuapp.com/)

## Overview
The Drunken Goblin in a site that provides users with a database to find, create, edit and share role playing characters. Allowing users to log in, view
their own characters, edit and remove them. But also contains a place where all characters stored into the database can be seen.

## Table of Contents

[UX](#ux)

[Features](#features)

[Technologies Used](#technologies)

[Testing](#testing)

[Deployment](#deployment)

[Credits](#credits)

<a name="UX"></a>

## UX
### User Stories
#### A First Time Visitor
- I want to be able to navigate the site easily and understand what it is for.
- I want to be able to look for role playing characters that suite my needs.
- I want to navigate the site easily, know what page I'm on be able to use the site to obtain all the information I need.
- I want to be able to create an account and create my own characters.

#### A Returning User
- I want to be able to log back into my account.
- I want to be able to see that characters that I have made then edit/delete them.
- I want to save characters that I did not make from other users in the database.
- I want to be able to sort/search for specific characters to fill me needs.

#### A User already with Dungeons and Dragons (D&D) knowledge
- I want to be able to create, edit and share characters that fit within the D&D specifications
- I want to see new and unusual characters that people have created that I can bring to my games.
- I want to see information on characters that I can use in my games and give me ideas for characters I would like to play.



### Strategy
- The aim of the website is to provide there users access to a database of characters to pick and chose from to take to their D&D games.
- The site allows users to create, edit and save characters with information such as 'Name', 'Class' and 'Race'.

### Scope
- Provide the user with a place to create, share and edit characters.
- Provide visitors with a clean and easy to navigate user interface.
- Allow users to sort through the characters available. 
- Provide users with the information they would need to use the characters in a game.

### Structure
#### Interaction Design
- Create a website that is responsive, works at all screen sizes and has mobile table and PC compatibility.
- Allow for easy navigation between pages of the website.
- Create easy to use and understand forms for users to fill in.
- Display created character information in an easy to read format.
#### Information Architecture
- Content is well structured, in line with the theme, easy to read and distinguish between.
- Content is spaced evenly and consistently throughout all screen sizes. 

### Skeleton
#### Wireframes

![Wireframes](/static/images/wireframes.jpg)

#### Information Design
- Information text is separated and spaced out to keep it clear easy to read.
- Information and forms with images in the background are also placed on a darker background with lighter text to help it stand out.
- All navigation links are easy to read and see.
- All Forms have appropriate labels so the user knows what they need to input.
- Created character information is labelled and spaced well on all screen sizes.

#### Interface Design
- The content is spaced well and its obvious where to go to proceed to the other pages on the site.
- All buttons are labelled and spaced well, so the user can see what page they will be sent too.

#### Navigation Design
- Navigation is located at the top of the page, the links the user will see is determined by their log in status.
- The user can also navigate using call to actions, or will be redirected after completing certain forms within the site.

### Surface
#### Typography
Two different fonts have been selected for use on this site. Both fonts have been obtained from [Google Fonts](https://fonts.google.com/).
- Raleway: Has been used for all text that is not a heading. This font is well spaced and easy to read with a more curved style.
- Cinzel: Has been used to all headings, a sharper text easy to read with a more fantasy style to fit the theme.


#### Colour Scheme

![Colour Pallet](/static/images/thedrunkengoblinpallet.jpg)


## Features
- The site is a multi-page site that includes a Home/Landing page, where the user and view the main page of the site the 'tavern', register and account or login.
- The 'Tavern' page is the main page of the site where all characters within the database are displayed. The idea is to display enough information for the user to 
    be able to use the characters in a game of D&D.
- There is a log in form on the landing page where the user will be 'logged in' and re-routed to their profile page.
- The profile page displays the characters the user has created, also showing the characters the user has saved.
- The create page is where the user can create a character of their own, where they will fill in a form with character details and upload an image of their character.
- The edit page is a close mirror of the create page, although the placeholder text will be shown as the details of the character chose to edit.
- The user can also log out and use the site to see all characters created but will not be able to create, edit or save characters.
#### Existing Features 
- Create- The user can create an account, where they can log in and view and experience the site with more features than a non logged in user.
    - The user can also create characters of their own, where they can choose the; name, image, race, class, likes, dislikes and backstory all in line with DnD rules.
- Read- On the tavern and profile pages the user can see the character information oh created characters straight from the data base.
- Update- Users can edit characters they have already created by selecting them from the user page.
- Delete- Users can also delete characters they have created, although not characters made by other users.
- Image upload- Upon creating a character the user will be required to upload an image.
    - The image is uploaded to 'cloudinary' using an API within the code. 
    - This image is then edit to a specific height and width and then converted into a url.
    - This url is saved within the data base in the character section and then loaded in the tavern and profile pages.          
- Search- The user will be able to search by character name, race and class on the tavern page.
- Save characters- Upon visiting the tavern page, the user will be able to save and store any characters they would like to quickly access.
    - These characters will be available on the users profile page under the characters they have made.



#### Features Left to Implement



<a name="technologies"></a>

## Technologies Used

### Languages
- HTML5: Used as the basic structure for Index/Play page, also used to create header element for all pages.
- CSS3: Used to style and structure all content.
- Java script: Used to provide all functionality for all aspects of the site including; game play and interactions, dynamically changing information
     displayed on pages and also for the intro sequence.
### Programs
- VS Code: Where all coding took place.
- Adobe XD: Used to create wireframes.
- Git Hub: Used to host the websites repository.
- Git Hub Desktop: Used to access the repository linking it to online Git Hub profile.
- IAmResponsive: Used to test responsiveness of site.
- Coolors: Used to display colour pallet used.
- [HTML Validator](https://validator.w3.org/) - Used to check HTML code for errors.
- [CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to check CSS code for errors.

<a name="Testing"></a>

## Testing

### Bugs
Intro sequence repeating when selecting the "play" nav element.
- Created a session storage loop that plays when the intro sequence first plays that prevents it from happening until page is exited then reloaded.

Images displaying incorrectly on smaller screen sizes.
- Created custom image sizes at different screen sizes using media queries, also centred the images.

Game not interacting as intended, questions not changing after each button press.
- Ensured there were no typos or spelling errors within the content.js file, created "i" variable using a loop that iterated through the object.

Player health not resetting after each game.
- After each game sequence reset the health of each faction to the correct value, in case the user wanted to play more than one round.

Game questions and answers displaying the wrong text.
- Ensured that all campaigns contained their own function and objects.

Local storage not accepting selected options until page had been refreshed.
- Moved the local storage save function within the document so it took place before the campaign selection function. Also added a local storage reset after each playthrough.

Question interactions repeating even after only one button press.
- Changed the question answer buttons from event listeners to "on-click" events, this meant that event listeners had to be removed after each question as the buttons were re-used multiple times
    and were in the function of the game.




### Nav Bar
- Checked that all links work correctly, taking the user to the desired page.
- Nav bar loads after the intro sequence, and upon refreshing into sequence does not run.

### Forces
- Check that upon clicking each faction separately the information is correct.
- Layout remains correct even when displaying assets with more or less text.

### Contact Us
- Both links work and submit correctly.
- Email validation works, only email addresses are allowed to be submitted.

### Play
#### Faction Selection
- Faction selection works as intended.
- Hovering over faction give a short summary of the faction.
- Local storage stores the faction selected.
- "Talking head" displays correct text cycles through the two sets of text and then remains hidden until page reload.
![TalkingHead](/assets/readme/talkinghead.jpg)

#### Enemy Selection
- Enemy selection works as intended.
- Hovering over enemy gives a short summary
- Local storage saves the enemy selected.
- "talking head" displays correct text and remains hidden upon clicking.

#### Game Screen
- Game loads correct, correct questions and answers are loaded dependant on which faction and enemy were selected.
- Game image loads correctly and different for which campaign was selected.
- Testing each option displays the correct damage and health, then loads the next set of question and answers.
- Tested using console.logs to display information within the code. 
![WorkingGame](/assets/readme/gameworking.jpg)

#### Victory/Defeat
- Victory page shows if player health is about 0 after the 5th and last question of the game.
- Defeat page shows when player health reaches 0. Displays correctly.
- Local storage is cleared after each round of the game to reset the faction and enemy.
![LoseGame](/assets/readme/losegame.jpg)
![LocalStorage](/assets/readme/localstoragereset.jpg)

### Code Validators
- HTML Validator shows no errors.
![HTML](/assets/readme/htmlchecker.jpg)

- CSS Validator shows no errors.
![CSS](/assets/readme/csschecker.jpg)

### Devices
- Galaxy S9: Works as intended.
- Galaxy S20: Works as intended.
- I phone 6: Works as intended.
- I phone 11: Works as intended.
- I Pad:  Works as intended.
- Small screen laptop: Works as intended.
- Large screen laptop: Works as intended.
- Desktop:  Works as intended.

### Browsers 
- Firefox: Working as intended no errors.
- Microsoft Edge: Working as intended no errors.
- Chrome: Working as intended no errors.
- Safari: Working as intended no errors.

<a name="Deployment"></a>

## Deployment

### Deployment to Github
1. Created new file inside documents folder named "Coding Course" and within that created a file called "Javascriptus-Crusade(Milestone Project 2)"
2. Opened GitHub Desktop and selected "New Repository"
3. Gave the project name "Sharks-Under-Threat" and clicked "Create Repository"
4. Opened the repository in VS Code
5. Created index.html and README.md pages
6. Opened up local terminal and "Git Added" both pages.
7. Committed both pages using "Git Commit".
8. Pushed changed with "Git Push" adding my work to my Git Hub page.
9. Opened my GitHib page to see the changes.

### How to fork the project

### Deployment to Heroku


<a name="credits"></a>

## Credits

### Technical


 ### Content 


 

 
 ### Images


 ### Acknowledgements
- Code Institute - Running the course and providing this opportunity. 
- Maranatha Ilesanmi (Mentor) - Feedback and support during the project. 
- Slack Community - Peer reviewing my work. 

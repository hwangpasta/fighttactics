# fighttactics

5/5/2020

-Turns out the League info for champions and whatnot is not located on an API, but are just given by Riot in a zip file. 
So...that could make things a lot easier. This file can be included into the program itself. 

General Plan (including up to the final deadline)

-Read in the json files with champions, items, and traits
  -Include the raw files that are publically accessible 
    -Read in the files correctly
    -create Champion objects to be stored, Item objects
      -HTML table for Champion
    -add a search bar to allow quick access to a champion page or items page
    
-Each champion has it's own link, should display a general info blurb about the champion (probably needs to come from another source)
-I want to try to do a drag and drop interface where it will adjust the damage calculations accordingly based on the traits acting among the champions https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API
-Actual battle simulations are probably outside of the scope of the project due date but could be doable in the future

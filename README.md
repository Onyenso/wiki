# Wiki
Wiki is an online encyclopedia where topics are cretaed and written about by users. Entries (topics) are written using Markdown, then the application converts the to
appropriate HTML for display. It was built using Python (Django), HTML and CSS.

### Project Description
The homepage displays all avalaible topics alphabetically. Initially, these are just sample topics with little contents. A user can create a new topic by clicking
[Create New Page](/encyclopedia/templates/encyclopedia/create.html) on the sidebar. This takes to a page that has a form that accepts Markdown content. After submission,
the topic is added to the list of topics in the encyclopedia.

<p>
[views.py](/encyclopedia/views.py) defines the functions for all of the routes. The folder, [templates](/encyclopedia/templates/encyclopedia) holds the front-end HTML
files. [entries](/entries) folder is where the Markdown contents of topics are saved when they are submitted. The project uses no databases and aesthetics are not most
important.
</p>

A video of this application's demonstration is at https://youtu.be/IJzDRupPgHA

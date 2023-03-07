# MS Teams Status Updater

A Flask web application that updates my Microsoft Teams Status and Status Message according to the work I am busy with.

## Application Context
As a developer working on multiple projects/applications, each with different client (internal), without the clients being aware of the project I am working on at any given moment, they can come to me with queries on their projects.  This interruption can be highly disruptive when focussing, not only does it break my concentration and flow, but I am also not imediately able to assist the client as I need to task switch and shift my thinking to their project.

Due to this, I have developed this application that updates my MS Teams Status and Status Message according to the work I am busy with.  This allows the various clients more insight into when a good time is to discuss their queries or bugs.

## Application Overview
The MS Teams Status Updater is a web app that I run on my local host, which allows me to update my status on Teams with a single click of a button. I just fill in a couple of checkboxes about the project that I am working on and the web app updatest my Teams status accordingly.


### Process
The MS Teams Status Updater homepage, allows the user to chose a project from a pre-configured set of projects.  The user selects the project they are working on, provides some additional information on the Category and Sub-Category and submits the update.  The app also allows the user to reset their status if no status is required.

<homepage image>

#### Status Update
- Graph API no functionality for Status updates
- Using selenium

#### Setup
- Start up (chrome - local host $ login to teams (MFA,))
  <images>
- Config



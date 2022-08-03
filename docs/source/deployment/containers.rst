Managing Raven Containers
=========================

During the course of deployment and use of the local demo you may wish
to bring your various Raven component containers up and down,
particularly if you wish to free up resources or ports or if you simply
need to delete a container entirely.

Note that there are some dependencies between the containers, at least
in function even if a component will still seemingly be operational. The
hierarchy of requirements is the order in which the containers are
deployed in the instructions, and is as follows, with default container
names given in parenthesis.

-  Fhirbase (fhir_db) - This container is the foundation of the entire
   stack, and is explicitly required by the Raven FHIR Server. It should
   be the first container brought up and the last container brought
   down.

-  Raven FHIR Server (raven-fhir-server) - This container sits on top of
   the Fhirbase fhir_db container directly, and so should be the second
   container to be brought up and second to last container brought down.

-  Raven Import and Submission API (raven-import-submit) - This
   container includes multiple APIs and acts as a go-between the
   Dashboard and other components or external servers. It can exist
   separately from other components without causing startup errors so
   does not have to be brought up in a strict order, but without the
   FHIR Server and database in turn it will not provide any
   functionality.

-  Raven Dashboard (raven-dashboard) - This should logically be the last
   component to be brought up and first component to be brought down.
   Like the Import and Submission APIs it will not encounter any startup
   errors if the other components are not present, but you may run into
   issues around browser caching that are better to avoid.

Data Persistance
----------------

**Please note that deleting the Fhirbase (fhir_db) container will
permanently remove any data you have posted to it through the FHIR
Server.** You may however **stop** the container without deleting it and
still retain your data.

When upgrading to newer versions of other Raven components, you may
leave your database container intact if there were no direct alterations
made to the database schema, maintaining your existing data. For
example, if there are updates to the Dashboard or APIs it is safe to
redeploy those without touching your database. This also applies to most
modifications to the Raven FHIR Server, as modification of the database
schema as present in the database itself is rare. In the case there is a
change in this regard, it will be called out explicitly.

If you wish to remove all of your data stored in the Fhirbase (fhir_db)
container, deleting the container and rerunning it through Docker is the
most efficient way to do so. For more fine tuned management, you will
want to use traditional FHIR operations which are outside of the scope
of this guide.

Managing Containers through a Command Line Interface
----------------------------------------------------

Starting Containers
~~~~~~~~~~~~~~~~~~~

Please note that this section only discusses starting containers in the
context of them having already been built and ran. If you need to
perform either of these steps, please consult the related section of
this deployment guide.

If your container has already been built and ran but you later stopped
it for some reason, you may start the container back up with the
following command, using the Raven Dashboard as an example:

::

   docker start raven-dashboard

For the other components, you would simply replace “raven-dashboard”
with the name of the component container.

Stopping Containers
~~~~~~~~~~~~~~~~~~~

To stop a running container, you simply need to execute the following
command:

::

   docker stop raven-dashboard

This will leave the container in a suspended state without deleting it.
Again, replace “raven-dashboard” with the name of the component
container.

Deleting/Removing Containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Please see the section on Data Persistence before permanently deleting
a container.**

If you need to delete a container permanently, you may do so by running
the following command:

::

   docker rm raven-dashboard

Again replacing “raven-dashboard” with the name of the specific
component container you wish to delete. This will note delete the image
the container is based on, only the actively inflated container. Once a
container is deleted, if you wish to run it again you will need to first
execute the “docker run” command as specified in the deployment guide
for that component, which will inflate the container based on the
settings specified in the command parameters and then start the
container.

Deleting Images
^^^^^^^^^^^^^^^

If you wish to permanently remove an image, you may execute the
following command:

::

   docker rmi raven-dashboard

While you will also be replacing “raven-dashboard” with the name of a
specific component image, please be aware that container names and image
names are rarely equivalent. For Raven most of the components maintain
the same naming scheme for the sake of simplicity and due the fact there
is no expectation a single system will ever need to run multiple
containers based on the same Raven images, though this is often not the
case. This can be seen with the Fhirbase fhir_db container, as the image
it is based on is actually a generic Fhirbase image and not Raven
specific prior to the database configuration performed as part of the
deployment. If you do not need that image anymore, you should use the
image name “fhirbase/fhirbase” in the “docker rmi” command.

Managing Containers through Docker Desktop
------------------------------------------

Docker Desktop, available for Windows and Mac OSX, allows for stopping,
starting, and removing containers through a GUI.

By selecting the “containers/apps” option in the Docker Desktop
dashboard view you will see a list of both currently running and stopped
containers. Hovering over a container will provide traditional “Play”
and “Stop” controls which will allow you manage the container.

The “images” option shows a list of currently built locally or
downloaded images. Hovering over each container in the list will show an
options icon of three stacked dots. Clicking this opens options to
inspect the image (such as the build commands from the Dockerfile),
along with additional advanced functionality which is out of the scope
of this guide. This list also includes the “remove” option, allowing you
delete the image from your local disk. Please note that while you can
run images from this list to inflate it into a container, it is not
recommended as there are certain arguments that the Raven Deployment
expects from the command line.

Step 4 - Deploy the Raven Dashboard
===================================

First, navigate to the /raven-dashboard subdirectory under
/raven-platform.

::

   # If you are in the Raven Mapper Export component directory, first use...
   cd ..

   # Otherwise, from the Raven Platform directory navigate to the Raven Dashboard with...
   cd raven-dashboard

Configuring the Dashboard
-------------------------

Unlike the other components, the environment variables are set in the
.env file you should find at the dashboard’s root directory. Two
variables will be defined. For your local deployment, ensure they are as
follows aside from any changes you need to make to reflect deviations
from this tutorial.

::

   FHIR_SERVER_URL=http://localhost:8080/raven-fhir-server/fhir
   MAPPER_EXPORT_URL=http://localhost:8081/raven-import-and-submit-api/

Running the Dashboard in Docker
-------------------------------

As with other components, the Dashboard is provided in a Docker
container which can be built and run with the following commands.

::

   sudo docker build -f Dockerfile.local -t raven-dashboard . 
   sudo docker run -d -p 80:80 --network=raven-platform --name raven-dashboard --restart unless-stopped raven-dashboard:latest

After the container is ran, you should be able to browse to
[[http://localhost:80/app/cases]] and see the browse cases view of the
Raven Dashboard. If you previously loaded a case through the health
check portion of the Raven Mapper Export component step you should see
this case reflected here, otherwise the list will be empty.

--------------

**Congratulations, you have successfully deployed the Raven Platform!**

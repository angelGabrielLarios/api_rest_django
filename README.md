# Documentaición de API REST con DJANGO y VideoIndexer



## Recursos de apoyo
Este proyecto se baso en esto

- [Video de Fazt Web sobre Django](https://www.youtube.com/watch?v=GE0Q8YNKNgs&t=1228s&pp=ygUPZGphbmdvIGZhenQgd2Vi )
- [Documentación de Django](https://www.djangoproject.com/)
- [Documentación de Django Rest Framework](https://www.django-rest-framework.org/)
- [Repositorio de github de Python con Video Indexer](https://github.com/Azure-Samples/azure-video-indexer-samples/tree/master/API-Samples/Python)



## Requerimientos para utilizar en proyecto
 - Utilizar visual studio code (el del icono azul) 

 <img src="docs/images/visual_studio_code_image.png" alt="Texto Alternativo" width="50" >


 - Para abrir el archivo README.md en **visual studio code**, dar click en el icono con una lupa que se encuentra 
 arriba a la derecha del editor
 
 ![texto alternativo](docs/images/open_readme.png)

 - el archivo una vez que le diste click al boton de la lupa se vera asi

 ![texto alternativo](docs/images/view_readme.png)

 - tener instalado `pip` en tu PC, si no lo tienes intalado investigar ¿como instalar `pip`?


 ## ¿Cómo ejecutar este proyecto?

- ejecutar para instalar las `dependencias` de este proyecto

````bash
pip install -r requirements.txt
````

- Despues, debes subir tu video a la portal de video indexer [https://www.videoindexer.ai/media/library](https://www.videoindexer.ai/media/library)


![alt text](docs/images/portal_videoindexer.png)

- Copiar el id del video indexado asi:

![alt text](docs/images/videoindexer_copy_id.png)

- El repositorio/proyecto tine un archivo de nombre `.env.example` ese archivo se va copiar nuevamente y camibiarlo a nombre solo `.env`

![alt text](docs/images/envs.png)


- Ahora el id del video que copiaron en el portal de videoindexer lo van pegar en esta variable que se llama `video_id` del archivo `.env`

![alt text](docs/images/variables_envs.png)

## ¿Como obtener las crendenciales de Video Indexer para las variables de entorno?
- ahora para las variables de `AccountName`, `ResourceGroup` y `SubscriptionId`, se obtiene al crear el recurso de Azure de nombre `Azure AI Video Indexer`

![alt text](docs/images/get_crendiants_videoindexer.png)


## ¿Como obtener las crendenciales de Video Indexer para las variables de entorno?

- ahora para la siguiente variables de entorno
    - `AZURE_OPENAI_API_KEY=`
    - `AZURE_OPENAI_ENDPOINT=`
    - `AZURE_OPENAI_API_VERSION`
    - `DEPLOYED_MODEL_NAME=`

 - `AZURE_OPENAI_API_VERSION` ya tiene un valor por defecto que es `2024-05-01-preview` pero puede cambiar a medida que pase el tiempo, consultar esto en [https://learn.microsoft.com/en-us/azure/ai-services/openai/reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)


- Para obtener `AZURE_OPENAI_API_KEY=``, AZURE_OPENAI_ENDPOINT=`, `AZURE_OPENAI_API_VERSION` se encuentra la info en esta imagen de tu servicio de Azure **Azure Open AI**

![alt text](docs/images/get_crendentials_openai.png)


- Para obtener `DEPLOYED_MODEL_NAME` debes desplegar un modelo en [https://oai.azure.com/](https://oai.azure.com/) con e inicar sesión con tu cuenta de Azure y vincularlo con tu servicio de Azure Open AI que creaste

- Desplegar el modelo aqui:
![alt text](docs/images/get_deploy_model_name.png)

- Copiar el nombre de tu modelo desplegado para la ultima variable

![alt text](docs/images/copy_name_model.png)

## Ejecutar el proyecto
- Abrir la terminal de visual studio code con `ctrl + j` o buscar `¿Cómo abrir una nueva terminal de Visual Studio Code`


- Ejeuctar estos de comandos de python

~~~bash
python manage.py makemigrations
~~~

~~~bash
python manage.py migrate
~~~


````bash
python .\manage.py runserver
````

 - si se ejecuto correctamente aparecera esto en la pantalla

 ![alt text](docs/images/out_runserver_django.png)

 - La dirección URL que te aparece en la consola te vas a dirigir ahi a tu navegador y debes acceder a esta ruta [http://127.0.0.1:8000/api/generate-minutes-of-video-meeting](http://127.0.0.1:8000/api/generate-minutes-of-video-meeting)

- Debes esperar un rato a que cargue la pagina y se descargará la minuta

# Notas
Por el momento se descarga un archivo markdown de extensión `.md` 

 

 
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


- ahora para las variables de `AccountName`, `ResourceGroup` y `SubscriptionId`, se obtiene al crear el recurso de Azure de nombre `Azure AI Video Indexer`

![alt text](docs/images/get_crendiants_videoindexer.png)

## Ejecutar el proyecto
- Abrir la terminal de visual studio code con `ctrl + j` o buscar `¿Cómo abrir una nueva terminal de Visual Studio Code`

````bash
python .\manage.py runserver
````

 - si se ejecuto correctamente aparecera esto en la pantalla

 ![alt text](docs/images/out_runserver_django.png)

 - La dirección URL que te aparece en la consola te vas a dirigir ahi a tu navegador y debes acceder a esta ruta [http://127.0.0.1:8000/api/get-video-transcript/?format=json]

- Debe aparecer este json o parecido a esto

 ![alt text](docs/images/request_api_endpoint_get_video_transcript.png)

 
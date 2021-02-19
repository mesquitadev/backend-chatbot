
import aiml
import os
from rest_framework import routers
from core.api.viewsets import PacienteViewSet
from consulta.api.viewsets import ConsultasViewSet
from medicamentos.api.viewsets import MedicamentosViewSet
router = routers.DefaultRouter()
#from aiml import kernel

class Brain():      

    def cerebro(self):
        os.chdir('C:/Users/Ewerton&Talita/Desktop/AIML') 
        
        kernel = aiml.Kernel()

        if os.path.isfile("bot_brain.brn"):
            kernel.bootstrap(brainFile="bot_brain.brn")

        else:
            kernel.bootstrap(learnFiles="core/std-startup.xml", commands="load aiml b")
            kernel.saveBrain("bot_brain.brn")   
      
        while True:
            frase=''  #criar a rota para ouvir

            if frase == "sair":

                exit()

            if frase == "salvar":

                kernel.saveBrain("bot_brain.brn")

            if frase == "2":

                router.register(r'medicamentos', MedicamentosViewSet)
                # rota cadastro de medicamento
            if frase == "3":

                router.register(r'consulta', ConsultasViewSet)  # rota cadastro de

            if frase == "4":

                router.register(r'paciente', PacienteViewSet)  # rota

            else:

                respond = kernel.respond(frase)

                print(respond)
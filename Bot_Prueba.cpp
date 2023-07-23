#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
    ifstream inputFile("Archivo_madre.sdf");
    ofstream archivo1("Resultados_Bot.txt");
    // ofstream archivo2("compuesto2.txt");
    int flag = 0;  //Se activa cuando encuentra "LTS" y se desactiva cuando encuentra "$$$$"
    int contador = 0;
    string line;
    if (inputFile.is_open() and archivo1.is_open()){
        while (getline(inputFile, line)){
            if (flag == 1){  //Si la bandera esta levantada...
                contador++;         //suma 1 al contador y comprueba el if 
                if (contador == 3){         //si el if es verdadero, significa que pasaron 3 lineas desde el "LTS"  
                archivo1<<line;   //copia la linea actual al nuevo archivo
                flag = 0;       //baja la bandera hasta que se encuentre un nuevo LTS
                contador = 0;   //Resetea el contador hasta que se encuentre un nuevo LTS
                archivo1<<endl;
                }
            }

            if (line.find("LTS") != string::npos){
                archivo1<<line;
                flag = 1;
                archivo1<<",";

            }   
        }
    }else{
        cout<<"No se pudieron abrir los archivos :(";
    }
//poner mensaje de exito!  
return 0;
}
import javax.swing.*;

public class Ajedrez01 {

    //Atributos o variables de clase
    private char tablero [][];
    private int n;
    private boolean amenaza;

    //Métodos
    public static void main(String[] x) {
        new Ajedrez01();
    }

    public Ajedrez01(){
        this.New_Menu();
    }

    private void New_Menu(){
        int Option;

        do{
            Option = Integer.parseInt(JOptionPane.showInputDialog(
                "----- Fichas -----\n" +
                "1. Configurar\n" +
                "2. Poner fichas\n" +
                "3. Evaluar amenazas\n" +
                "0. Salir\n" +
                "Ingrese su opción:"
            ));
            switch(Option){
                case 1:
                    this.tablero();
                    this.rey();
                    break;
                case 2:
                    this.caballo();
                    this.torre();
                    this.alfil();
                    break;
                case 3:
                    evaluaramenazas();
                    break;
                case 0:
                    JOptionPane.showMessageDialog(null,"Gracias por jugar");
                    break;
                default:
                    JOptionPane.showMessageDialog(null,"Opción no valida");
                    break;
            }
        } while (Option != 0);
    }

    // private void menú(){

    //     int opción;

    //     do {
    //         opción = Integer.parseInt(JOptionPane.showInputDialog("--OPCIONES-- \n"+
    //                 "1. Caballo\n"+
    //                 "2. Torre\n"+
    //                 "3. Alfil\n"+
    //                 "0. Atrás\n"));
    //         switch (opción){
    //             case 1:
    //                 this.caballo();
    //                 break;
    //             case 2:
    //                 this.torre();
    //                 break;
    //             case 3:
    //                 this.alfil();
    //                 break;
    //             case 0:
    //                 JOptionPane.showMessageDialog(null,"Gracias por jugar");
    //                 break;
    //             default:
    //                 JOptionPane.showMessageDialog(null,"Opción no valida");
    //                 break;
    //         }
    //     }
    //     while (opción != 0);
    // }

    private void tablero(){

        n = Integer.parseInt(JOptionPane.showInputDialog("Digite el tamaño del tablero: "));
        tablero = new char[n][n];

        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                tablero [i][j] = '*';
            }
        }
    }

    private void rey(){

        int fR,cR;

        fR = (int)(Math.random()*n);
        cR = (int)(Math.random()*n);
        tablero[fR][cR] = 'R';

        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                System.out.print(tablero [i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("--------------------");
    }

    private void caballo(){

        int x,y,f,c;

        do {
            do {
                x = (int)(Math.random()*n);
                if (x<0 || x>n-1)
                    JOptionPane.showMessageDialog(null, "La fila está por fuera");
            }
            while (x<0 || x>n-1);
            do {
                y = (int)(Math.random()*n);
                if (y<0 || y>n-1)
                    JOptionPane.showMessageDialog(null, "La columna está por fuera");
            }
            while (y<0 || y>n-1);
            if (tablero[x][y]=='*'){
                tablero[x][y] = 'C';
                break;
            }
            else
                JOptionPane.showMessageDialog(null, "La casilla está ocupada");
        }
        while (tablero[x][y] != '*');


        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                System.out.print(tablero [i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("--------------------");

        //Evaluación de amenazas
        amenaza = false;

        //Caso 1
        f = x-2;
        c = y+1;
        if (f>=0 && f<n && c>=0 && c<n){
            if (tablero[f][c]=='R') {
                amenaza = true;
            }
        }
        //Caso 2
        if (amenaza==false){
            f = x-1;
            c = y+2;
            if (f>=0 && f<n && c>=0 && c<n){
                if (tablero[f][c]=='R')
                    amenaza = true;
            }
        }
        //Caso 3
        if (amenaza==false){
            f = x+1;
            c = y+2;
            if (f>=0 && f<n && c>=0 && c<n){
                if (tablero[f][c]=='R')
                    amenaza = true;
            }
        }
        //Caso 4
        if (amenaza==false){
            f = x+2;
            c = y+1;
            if (f>=0 && f<n && c>=0 && c<n){
                if (tablero[f][c]=='R')
                    amenaza = true;
            }
        }
        //Caso 5
        if (amenaza==false){
            f = x+2;
            c = y-1;
            if (f>=0 && f<n && c>=0 && c<n){
                if (tablero[f][c]=='R')
                    amenaza = true;
            }
        }
        //Caso 6
        if (amenaza==false){
            f = x+1;
            c = y-2;
            if (f>=0 && f<n && c>=0 && c<n){
                if (tablero[f][c]=='R')
                    amenaza = true;
            }
        }
        //Caso 7
        if (amenaza==false){
            f = x-1;
            c = y-2;
            if (f>=0 && f<n && c>=0 && c<n){
                if (tablero[f][c]=='R')
                    amenaza = true;
            }
        }
        //Caso 8
        if (amenaza==false){
            f = x-2;
            c = y-1;
            if (f>=0 && f<n && c>=0 && c<n){
                if (tablero[f][c]=='R')
                    amenaza = true;
            }
        }
    }

    private void torre() {

        int x,y,cont=1;

        do {
            do {
                x = (int)(Math.random()*n);
                if (x<0 || x>n-1)
                    JOptionPane.showMessageDialog(null, "La fila está por fuera");
            }
            while (x<0 || x>n-1);
            do {
                y = (int)(Math.random()*n);
                if (y<0 || y>n-1)
                    JOptionPane.showMessageDialog(null, "La columna está por fuera");
            }
            while (y<0 || y>n-1);
            if (tablero[x][y]=='*'){
                tablero[x][y] = 'T';
                break;
            }
            else
                JOptionPane.showMessageDialog(null, "La casilla está ocupada");
        }
        while (tablero[x][y] != '*');

        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                System.out.print(tablero [i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("--------------------");

        // Evaluación de amenazas
        amenaza = false;
    
        // Caso 1: Evaluación hacia arriba
        x = x - cont;
        while (x >= 0) {
            if (tablero[x][y] == 'R') {
                amenaza = true;
                break;
            } else if (tablero[x][y] != '*') {
                break;
            }
            x = x - cont;
        }
    
        // Caso 2: Evaluación hacia abajo
        x = x + cont;
        while (x < n) {
            if (tablero[x][y] == 'R') {
                amenaza = true;
                break;
            } else if (tablero[x][y] != '*') {
                break;
            }
            x = x + cont;
        }
    
        // Caso 3: Evaluación hacia la izquierda
        x = x - cont;
        y = y - cont;
        while (y >= 0) {
            if (tablero[x][y] == 'R') {
                amenaza = true;
                break;
            } else if (tablero[x][y] != '*') {
                break;
            }
            y = y - cont;
        }
    
        // Caso 4: Evaluación hacia la derecha
        y = y + cont;
        while (y < n) {
            if (tablero[x][y] == 'R') {
                amenaza = true;
                break;
            } else if (tablero[x][y] != '*') {
                break;
            }
            y = y + cont;
        }

    }
    
    private void alfil() {
        int x, y, cont = 1;
    
        do {
            do {
                x = (int)(Math.random()*n);
                if (x < 0 || x > n - 1)
                    JOptionPane.showMessageDialog(null, "La fila está por fuera");
            } while (x < 0 || x > n - 1);
    
            do {
                y = (int)(Math.random()*n);
                if (y < 0 || y > n - 1)
                    JOptionPane.showMessageDialog(null, "La columna está por fuera");
            } while (y < 0 || y > n - 1);
    
            if (tablero[x][y] == '*') {
                tablero[x][y] = 'A';
                break;
            } else {
                JOptionPane.showMessageDialog(null, "La casilla está ocupada");
            }
        } while (tablero[x][y] != '*');
    
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(tablero[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("--------------------");
    
        // Evaluación de amenazas
        // Caso 1
        boolean amenaza = false;
        int tempX = x, tempY = y;
        cont = 1;
    
        while (tempX - cont >= 0 && tempY + cont < n) {
            tempX = x - cont;
            tempY = y + cont;
    
            if (tablero[tempX][tempY] != '*') {
                if (tablero[tempX][tempY] == 'R') {
                    amenaza = true;
                    break;
                }
            }
            cont++;
        }
    
        // Caso 2
        if (!amenaza) {
            cont = 1;
            tempX = x;
            tempY = y;
    
            while (tempX + cont < n && tempY + cont < n) {
                tempX = x + cont;
                tempY = y + cont;
    
                if (tablero[tempX][tempY] != '*') {
                    if (tablero[tempX][tempY] == 'R') {
                        amenaza = true;
                        break;
                    }
                }
                cont++;
            }
        }
    
        // Caso 3
        if (!amenaza) {
            cont = 1;
            tempX = x;
            tempY = y;
    
            while (tempX + cont < n && tempY - cont >= 0) {
                tempX = x + cont;
                tempY = y - cont;
    
                if (tablero[tempX][tempY] != '*') {
                    if (tablero[tempX][tempY] == 'R') {
                        amenaza = true;
                        break;
                    }
                }
                cont++;
            }
        }
    
        // Caso 4
        if (!amenaza) {
            cont = 1;
            tempX = x;
            tempY = y;
    
            while (tempX - cont >= 0 && tempY - cont >= 0) {
                tempX = x - cont;
                tempY = y - cont;
    
                if (tablero[tempX][tempY] != '*') {
                    if (tablero[tempX][tempY] == 'R') {
                        amenaza = true;
                        break;
                    }
                }
                cont++;
            }
        }
    }
    
    private void evaluaramenazas() {
        boolean amenaza = false;
        int reyFila = -1;
        int reyColumna = -1;

        // Encontrar la posición del rey en el tablero
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (tablero[i][j] == 'R') {
                    reyFila = i;
                    reyColumna = j;
                    break;
                }
            }
        }

        // Verificar amenazas por fichas de caballo
        
        if (!amenaza) {
            // Verificar amenazas por fichas de torre
            amenaza = AmenazaCaballo(reyFila, reyColumna);
            if (amenaza){
                JOptionPane.showMessageDialog(null, "El rey está amenazado por el caballo.");
            } else {
                JOptionPane.showMessageDialog(null, "El rey no está amenazado por el caballo.");
            }


            // Verificar amenazas por fichas de torre
            amenaza = AmenazaTorre(reyFila, reyColumna);
            if (amenaza){
                JOptionPane.showMessageDialog(null, "El rey está amenazado por la torre.");
            } else {
                JOptionPane.showMessageDialog(null, "El rey no está amenazado por la torre.");
            }

            // Verificar amenazas por fichas de alfil
            amenaza = AmenazaAlfil(reyFila, reyColumna);
            if (amenaza){
                JOptionPane.showMessageDialog(null, "El rey está amenazado por el alfil.");
            } else {
                JOptionPane.showMessageDialog(null, "El rey no está amenazado por el alfil.");
            }
        } else {
            JOptionPane.showMessageDialog(null, "No hay amenazas al rey.");
        }
    }

    private boolean AmenazaCaballo(int reyFila, int reyColumna) {
        int[][] movimientosCaballo = { { -2, 1 }, { -1, 2 }, { 1, 2 }, { 2, 1 }, { 2, -1 }, { 1, -2 }, { -1, -2 }, { -2, -1 } };

        for (int[] movimiento : movimientosCaballo) {
            int nuevaFila = reyFila + movimiento[0];
            int nuevaColumna = reyColumna + movimiento[1];

            if (PosicionValida(nuevaFila, nuevaColumna) && tablero[nuevaFila][nuevaColumna] == 'C') {
                return true;
            }
        }

        return false;
    }

    private boolean AmenazaTorre(int reyFila, int reyColumna) {
        // Verificar amenaza por filas y columnas
        for (int i = 0; i < n; i++) {
            if (tablero[reyFila][i] == 'T' || tablero[i][reyColumna] == 'T') {
                return true;
            }
        }

        return false;
    }

    private boolean AmenazaAlfil(int reyFila, int reyColumna) {
        // Verificar amenaza por diagonales
        int[][] movimientosAlfil = { { -1, -1 }, { -1, 1 }, { 1, -1 }, { 1, 1 } };

        for (int[] movimiento : movimientosAlfil) {
            int nuevaFila = reyFila + movimiento[0];
            int nuevaColumna = reyColumna + movimiento[1];

            while (PosicionValida(nuevaFila, nuevaColumna)) {
                if (tablero[nuevaFila][nuevaColumna] == 'A') {
                    return true;
                }
                nuevaFila += movimiento[0];
                nuevaColumna += movimiento[1];
            }
        }

        return false;
    }

    private boolean PosicionValida(int fila, int columna) {
        return fila >= 0 && fila < n && columna >= 0 && columna < n;
    }

}

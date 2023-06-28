import javax.swing.JOptionPane;

public class AjedrezTroncosoOscar {
    private char tablero[][];
    private int n;
    private boolean amenaza;


    public static void main(String[] xxx) {
        new AjedrezTroncosoOscar();
    }

    public AjedrezTroncosoOscar() {
        this.menu();
    }

    private void menu() {
        int opcion;
        do {
            opcion = Integer.parseInt(JOptionPane.showInputDialog("Fichas\n" +
                    "1. Configurar\n" +
                    "2. Poner fichas\n" +
                    "3. Evaluar\n" +
                    "0. Salir\n"));
            switch (opcion) {
                case 1:
                    this.Configurar();
                    this.Rey();
                    break;
                case 2:
                    this.Ponerfichas();
                    break;
                case 3:
                    this.Evaluar();
                    break;
                case 0:
                    this.Salir();
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Opción no válida");
                    break;
            }
        } while (opcion != 0);
    }

    private void Configurar() {

        n = Integer.parseInt(JOptionPane.showInputDialog("Digite el tamaño del tablero: "));
        tablero = new char[n][n];

        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                tablero [i][j] = '*';
            }
        }
    }

    private void Ponerfichas() {
        // for (int i = 0; i < n; i++) {
        //     for (int j = 0; j < n; j++) {
        //         if (tablero[i][j] == '*') {
        //             System.out.print(" * ");
        //         } else {
        //             System.out.print(" " + tablero[i][j] + " ");
        //         }
        //     }
        //     System.out.println();
        // }
        this.Caballo();
        this.Alfil();
        this.Torre();
    }
    
    private void Rey() {
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
    
    private void Caballo(){

        int x,y,f,c;

        do {
            do {
                x = (int)(Math.random()*(n-1));
            }
            while (x<0 || x>n-1);
            do {
                y = (int)(Math.random()*(n-1));
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
        if (amenaza==true)
            JOptionPane.showMessageDialog(null, "El caballo amenaza al rey");
        else
            JOptionPane.showMessageDialog(null, "El caballo no amenaza al rey");
    }
    private void Torre(){

        int x,y,cont=1;

        do {
            do {
                x = (int)(Math.random()*(n-1));
            }
            while (x<0 || x>n-1);
            do {
                y = (int)(Math.random()*(n-1));
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

        //Evaluación de amenazas
        //Caso 1
        amenaza = false;
        do {
            x = x - cont;
            if (tablero[x][y]!= '*'){
                if (tablero [x][y] == 'R')
                    amenaza = true;
                break;
            }
            cont++;
        }
        while (x-cont>0 && y+cont<n);
        //Caso 2
        cont = 1;
        if (!amenaza){
            do {
                x = x + cont;
                if (tablero[x][y]!= '*'){
                    if (tablero [x][y] == 'R')
                        amenaza = true;
                    break;
                }
                cont++;
            }
            while (x+cont<n && y+cont<n);
        }
        //Caso 3
        cont = 1;
        if (!amenaza){
            do {
                y = y - cont;
                if (tablero[x][y]!= '*'){
                    if (tablero [x][y] == 'R')
                        amenaza = true;
                    break;
                }
                cont++;
            }
            while (x+cont<n && y-cont>0);
        }
        //Caso 4
        cont = 1;
        if (!amenaza){
            do {
                y = y + cont;
                if (tablero[x][y]!= '*'){
                    if (tablero [x][y] == 'R')
                        amenaza = true;
                    break;
                }
                cont++;
            }
            while (x-cont>0 && y-cont>0);
        }
        if (amenaza==true)
            JOptionPane.showMessageDialog(null, "La torre amenaza al rey");
        else
            JOptionPane.showMessageDialog(null, "La torre no amenaza al rey");
    }
    private void Alfil() {

        int x,y,cont=1;

        do {
            do {
                x = (int)(Math.random()*(n-1));
            }
            while (x < 0 || x > n - 1);
            do {
                y = (int)(Math.random()*(n-1));
            }
            while (y < 0 || y > n - 1);
            if (tablero[x][y] == '*') {
                tablero[x][y] = 'A';
                break;
            } else
                JOptionPane.showMessageDialog(null, "La casilla está ocupada");
        }
        while (tablero[x][y] != '*');

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(tablero[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("--------------------");

        //Evaluación de amenazas
        //Caso 1
        amenaza = false;
        do {
            x = x - cont;
            y = y + cont;
            if (tablero[x][y]!= '*'){
                if (tablero [x][y] == 'R')
                    amenaza = true;
                break;
            }
            cont++;
        }
        while (x-cont>0 && y+cont<n);
        //Caso 2
        cont = 1;
        if (!amenaza){
            do {
                x = x + cont;
                y = y + cont;
                if (tablero[x][y]!= '*'){
                    if (tablero [x][y] == 'R')
                        amenaza = true;
                    break;
                }
                cont++;
            }
            while (x+cont<n && y+cont<n);
        }
        //Caso 3
        cont = 1;
        if (!amenaza){
            do {
                x = x + cont;
                y = y - cont;
                if (tablero[x][y]!= '*'){
                    if (tablero [x][y] == 'R')
                        amenaza = true;
                    break;
                }
                cont++;
            }
            while (x+cont<n && y-cont>0);
        }
        //Caso 4
        cont = 1;
        if (!amenaza){
            do {
                x = x - cont;
                y = y - cont;
                if (tablero[x][y]!= '*'){
                    if (tablero [x][y] == 'R')
                        amenaza = true;
                    break;
                }
                cont++;
            }
            while (x-cont>0 && y-cont>0);
        }
        if (amenaza==true)
            JOptionPane.showMessageDialog(null, "El alfil amenaza al rey");
        else
            JOptionPane.showMessageDialog(null, "El alfil no amenaza al rey");

    }
   

    private void Evaluar() {
    
        // Verificar las amenazas
        boolean amenazaRey = false;
        boolean amenazaFichas = false;
        String fichaAmenazaRey = "";
        String fichasAmenazandose = "";

        // Verificar amenaza del caballo al rey
        int xCaballo = -1;
        int yCaballo = -1;
        int xTorre = -1;
        int yTorre = -1;
        int xAlfil = -1;
        int yAlfil = -1;

        // Buscar la posición del caballo en el tablero
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (tablero[i][j] == 'C') {
                    xCaballo = i;
                    yCaballo = j;
                    break;
                }
            }
            if (xCaballo != -1 && yCaballo != -1) {
                break;
            }
        }

        // Verificar amenaza del caballo al rey
        if (xCaballo != -1 && yCaballo != -1) {

            // Caso 1
            int f = xCaballo - 2;
            int c = yCaballo + 1;
            if (f >= 0 && f < n && c >= 0 && c < n && tablero[f][c] == 'R') {
                amenazaRey = true;
                fichaAmenazaRey = "Caballo";
            }

            // Caso 2
            f = xCaballo - 1;
            c = yCaballo + 2;
            if (!amenazaRey && f >= 0 && f < n && c >= 0 && c < n && tablero[f][c] == 'R') {
                amenazaRey = true;
                fichaAmenazaRey = "Caballo";
            }

            // Caso 3
            f = xCaballo + 1;
            c = yCaballo + 2;
            if (!amenazaRey && f >= 0 && f < n && c >= 0 && c < n && tablero[f][c] == 'R') {
                amenazaRey = true;
                fichaAmenazaRey = "Caballo";
            }

            // Caso 4
            f = xCaballo + 2;
            c = yCaballo - 1;
            if (!amenazaRey && f >= 0 && f < n && c >= 0 && c < n && tablero[f][c] == 'R') {
                amenazaRey = true;
                fichaAmenazaRey = "Caballo";
            }

            // Caso 5
            f = xCaballo + 2;
            c = yCaballo + 1;
            if (!amenazaRey && f >= 0 && f < n && c >= 0 && c < n && tablero[f][c] == 'R') {
                amenazaRey = true;
                fichaAmenazaRey = "Caballo";
            }

            // Caso 6
            f = xCaballo + 1;
            c = yCaballo - 2;
            if (!amenazaRey && f >= 0 && f < n && c >= 0 && c < n && tablero[f][c] == 'R') {
                amenazaRey = true;
                fichaAmenazaRey = "Caballo";
            }

            // Caso 7
            f = xCaballo - 1;
            c = yCaballo - 2;
            if (!amenazaRey && f >= 0 && f < n && c >= 0 && c < n && tablero[f][c] == 'R') {
                amenazaRey = true;
                fichaAmenazaRey = "Caballo";
            }

            // Caso 8
            f = xCaballo - 2;
            c = yCaballo - 1;
            if (!amenazaRey && f >= 0 && f < n && c >= 0 && c < n && tablero[f][c] == 'R') {
                amenazaRey = true;
                fichaAmenazaRey = "Caballo";
            }
        }

        // Buscar la posición de la torre y el alfil en el tablero
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (tablero[i][j] == 'T') {
                    xTorre = i;
                    yTorre = j;
                } else if (tablero[i][j] == 'A') {
                    xAlfil = i;
                    yAlfil = j;
                }

                if (xTorre != -1 && yTorre != -1 && xAlfil != -1 && yAlfil != -1) {
                    break;
                }
            }
            if (xTorre != -1 && yTorre != -1 && xAlfil != -1 && yAlfil != -1) {
                break;
            }
        }

        // Verificar amenaza de la torre al rey
        if (xTorre != -1 && yTorre != -1) {
            // Verificar amenaza horizontalmente hacia la derecha
            for (int j = yTorre + 1; j < n; j++) {
                if (tablero[xTorre][j] == 'R') {
                    amenazaRey = true;
                    fichaAmenazaRey = "Torre";
                    break;
                } else if (tablero[xTorre][j] != '*') {
                    amenazaFichas = true;
                    fichasAmenazandose = "Torre";
                    break;
                }
            }

            // Verificar amenaza horizontalmente hacia la izquierda
            for (int j = yTorre - 1; j >= 0; j--) {
                if (tablero[xTorre][j] == 'R') {
                    amenazaRey = true;
                    fichaAmenazaRey = "Torre";
                    break;
                } else if (tablero[xTorre][j] != '*') {
                    amenazaFichas = true;
                    fichasAmenazandose = "Torre";
                    break;
                }
            }

            // Verificar amenaza verticalmente hacia arriba
            for (int i = xTorre - 1; i >= 0; i--) {
                if (tablero[i][yTorre] == 'R') {
                    amenazaRey = true;
                    fichaAmenazaRey = "Torre";
                    break;
                } else if (tablero[i][yTorre] != '*') {
                    amenazaFichas = true;
                    fichasAmenazandose = "Torre";
                    break;
                }
            }

            // Verificar amenaza verticalmente hacia abajo
            for (int i = xTorre + 1; i < n; i++) {
                if (tablero[i][yTorre] == 'R') {
                    amenazaRey = true;
                    fichaAmenazaRey = "Torre";
                    break;
                } else if (tablero[i][yTorre] != '*') {
                    amenazaFichas = true;
                    fichasAmenazandose = "Torre";
                    break;
                }
            }
        }

        // Verificar amenaza del alfil al rey
        if (xAlfil != -1 && yAlfil != -1) {
            // Caso 1: diagonal hacia arriba y a la derecha
            int contador = 1;
            int f = xAlfil;
            int c = yAlfil;

            while (f - contador >= 0 && c + contador < n) {
                int x = f - contador;
                int y = c + contador;
                if (tablero[x][y] != '*') {
                    if (tablero[x][y] == 'R') {
                        amenazaRey = true;
                        fichaAmenazaRey = "Alfil";
                    } else {
                        amenazaFichas = true;
                        fichasAmenazandose = "Alfil";
                    }
                    break;
                }
                contador++;
            }

            // Caso 2: diagonal hacia abajo y a la derecha
            contador = 1;
            f = xAlfil;
            c = yAlfil;

            while (f + contador < n && c + contador < n) {
                int x = f + contador;
                int y = c + contador;
                if (tablero[x][y] != '*') {
                    if (tablero[x][y] == 'R') {
                        amenazaRey = true;
                        fichaAmenazaRey = "Alfil";
                    } else {
                        amenazaFichas = true;
                        fichasAmenazandose = "Alfil";
                    }
                    break;
                }
                contador++;
            }

            // Caso 3: diagonal hacia abajo y a la izquierda
            contador = 1;
            f = xAlfil;
            c = yAlfil;

            while (f + contador < n && c - contador >= 0) {
                int x = f + contador;
                int y = c - contador;
                if (tablero[x][y] != '*') {
                    if (tablero[x][y] == 'R') {
                        amenazaRey = true;
                        fichaAmenazaRey = "Alfil";
                    } else {
                        amenazaFichas = true;
                        fichasAmenazandose = "Alfil";
                    }
                    break;
                }
                contador++;
            }

            // Caso 4: diagonal hacia arriba y a la izquierda
            contador = 1;
            f = xAlfil;
            c = yAlfil;

            while (f - contador >= 0 && c - contador >= 0) {
                int x = f - contador;
                int y = c - contador;
                if (tablero[x][y] != '*') {
                    if (tablero[x][y] == 'R') {
                        amenazaRey = true;
                        fichaAmenazaRey = "Alfil";
                    } else {
                        amenazaFichas = true;
                        fichasAmenazandose = "Alfil";
                    }
                    break;
                }
                contador++;
            }
        }

        // Mostrar resultados
        if (amenazaRey) {
            JOptionPane.showMessageDialog(null, "El rey está amenazado por el " + fichaAmenazaRey + ".");
        } else {
            JOptionPane.showMessageDialog(null, "El rey no está amenazado.");
        }

        if (amenazaFichas) {
            JOptionPane.showMessageDialog(null, "Las fichas " + fichasAmenazandose + " se están amenazando entre sí.");
        } else {
            JOptionPane.showMessageDialog(null, "No hay fichas amenazándose entre sí.");
        }
    }
        
    private void Salir() {
        System.exit(0);
    }
}

import javax.swing.JOptionPane;


public class Ajedrez4 {
    private int n;


    private char tablero[][] = new char[n][n];
    private int posxR = (int)(Math.random()*n);
    private int posxY = (int)(Math.random()*n);
    private boolean amenaza;

    public static void main (String [] xxx){
        new Ajedrez4();
    }

    public Ajedrez4 (){
        this.menu();
        
    }

    private void menu (){
        int opcion;
        do{
            opcion = Integer.parseInt(JOptionPane.showInputDialog("Fichas\n"+
                                                                "1. Caballo\n"+
                                                                "2. Torre\n"+
                                                                "3. Alfil\n"+
                                                                "0. Salir\n"));
            switch (opcion){
                case 1:
                    this.caballo();
                    break;
                case 2:
                    this.Torre();
                    break;
                case 3:
                    this.Alfil();
                    break;
                case 0:
                    this.Salir();
                    break;
            }
        }
        while(opcion != 0);
    }

    private void Caballo(){

        for(int i = 0; i < n; i ++){
            for (int j = 0; j < n; j ++){
                System.out.print(tablero[i][j] + " * ");
            }
            System.out.println();
        }

        int x,y;
        do{
            do{
                x = Integer.parseInt (JOptionPane.showInputDialog("Digite fila"));
                if(x < 0 || x > n-1)
                    JOptionPane.showMessageDialog(null, "Esa fila esta por fuera");
            }

            while (x < 0 || x > n -1);

            do{
                y = Integer.parseInt (JOptionPane.showInputDialog("Digite columna"));
                if(y < 0 || y > n-1)
                    JOptionPane.showMessageDialog(null, "Esa columna esta por fuera");
            }

            while (y < 0 || y > n -1);


            if(tablero[x][y]== '*'){
                tablero[x][y]='C';
                break;
            }
            else 
                JOptionPane.showMessageDialog(null,"Casilla ya ocupada");
        }
        while(tablero[x][y] == '*');

        for(int i = 0; i < n; i ++){
            for (int j = 0; j < n; j ++){
                System.out.print(tablero[i][j] + " * ");
            }
            System.out.println();
        }
        System.out.println("===================================");
        // Evaluacion 
        // caso 1:
        JOptionPane.showMessageDialog(null,"Caso 1");
        amenaza = false;
        int f = x - 2;
        int c = y + 1;
        if(f >= 0 && f < n && c >= 0 && c<n)
        {
            if(tablero[f][c]=='R'){
                amenaza = true;
            }
            
        }

        // caso 2
        JOptionPane.showMessageDialog(null,"Caso 2");

        if(amenaza == false){
            f = x - 1;
            c = y + 2;
            if(f >= 0 && f<n && c>=0 && c<n)
            {
                if(tablero[f][c]=='R'){
                    amenaza = true;
                }
            } 
        }
        // caso 3
        JOptionPane.showMessageDialog(null,"Caso 3");

        if(amenaza == false){
            f = x + 1;
            c = y + 2;
            if(f >= 0 && f<n && c>=0 && c<n)
            {
                if(tablero[f][c]=='R'){
                    amenaza = true;
                }
            }
        }
        //Caso 4
        JOptionPane.showMessageDialog(null,"Caso 4");

        if(amenaza == false){
            f = x +2;
            c = y -1;
            if(f>=0 && f<n && c>=0 && c<n){
                if(tablero[f][c]=='R'){
                    amenaza = true;
                }
                
            }
        }
        // caso 5
        JOptionPane.showMessageDialog(null,"Caso 5");
        if(amenaza == false){
            f = x + 2;
            c = y - 1;
            if(f >= 0 && f<n && c>=0 && c<n)
            {
                if(tablero[f][c]=='R'){
                    amenaza = true;
                }
                
            }
        }
        // Caso 6
        JOptionPane.showMessageDialog(null,"Caso 6");
        if(amenaza == false){
            f = x + 1;
            c = y - 2;
            if(f >= 0 && f<n && c>=0 && c<n)
            {
                if(tablero[f][c]=='R'){
                    amenaza = true;
                }
                
            }
        }
        //caso 7
        JOptionPane.showMessageDialog(null,"Caso 7");
        if(amenaza == false){
            f = x - 1;
            c = y - 2;
            if(f >= 0 && f<n && c>=0 && c<n)
            {
                if(tablero[f][c]=='R'){
                    amenaza = true;
                }
                
            }
        }
        //caso 8 
        JOptionPane.showMessageDialog(null,"Caso 8");
        if(amenaza == false){
            f = x - 2;
            c = y - 1;
            if(f >= 0 && f<n && c>=0 && c<n)
            {
                if(tablero[f][c]=='R'){
                    amenaza = true;
                }
                
            }
        }
        if(amenaza==true)
            JOptionPane.showMessageDialog(null, "Esa ficha amenaza al rey ");
        else
            JOptionPane.showMessageDialog(null, "Esa ficha NO amenaza al rey ");    }
    
    private void Torre(){
        do{
            do{
                x = Integer.parseInt (JOptionPane.showInputDialog("Digite fila"));
                if(x<0 || x> n-1)
                    JOptionPane.showMessageDialog(null, "Esa fila esta por fuera");
            }
            while (x < 0 || x > n -1);
            do{
                x = Integer.parseInt (JOptionPane.showInputDialog("Digite columna"));
                if(y < 0 || y > n-1)
                    JOptionPane.showMessageDialog(null, "Esa columna esta por fuera");
            }
            while (y < 0 || y > n -1);

            if(tablero[x][y]== '*'){
                tablero[x][y]='T';
                break;
            }
            else 
                JOptionPane.showMessageDialog(null,"Casilla ya ocupada");
        }
        while(tablero[x][y] == '*');

        for(int i = 0; i < n; i ++){
            for (int j = 0; j < n; j ++){
                System.out.print(tablero[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("===================================");
        do {
            do {
                x = Integer.parseInt(JOptionPane.showInputDialog("Digite fila"));
                if (x < 0 || x > n - 1)
                    JOptionPane.showMessageDialog(null, "Esa fila está fuera de rango");
            } while (x < 0 || x > n - 1);
            do {
                y = Integer.parseInt(JOptionPane.showInputDialog("Digite columna"));
                if (y < 0 || y > n - 1)
                    JOptionPane.showMessageDialog(null, "Esa columna está fuera de rango");
            } while (y < 0 || y > n - 1);
    
            if (tablero[x][y] == '*') {
                tablero[x][y] = 'T';
                break;
            } else
                JOptionPane.showMessageDialog(null, "Casilla ya ocupada");
        } while (tablero[x][y] == '*');
    
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(tablero[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("===================================");
    
        // Evaluación de amenazas
        amenaza = false;
        // Verificar amenaza horizontalmente hacia la derecha
        for (int j = y + 1; j < n; j++) {
            if (tablero[x][j] == 'R') {
                amenaza = true;
                break;
            } else if (tablero[x][j] != '*') {
                break;
            }
        }
    
        // Verificar amenaza horizontalmente hacia la izquierda
        for (int j = y - 1; j >= 0; j--) {
            if (tablero[x][j] == 'R') {
                amenaza = true;
                break;
            } else if (tablero[x][j] != '*') {
                break;
            }
        }
    
        // Verificar amenaza verticalmente hacia arriba
        for (int i = x - 1; i >= 0; i--) {
            if (tablero[i][y] == 'R') {
                amenaza = true;
                break;
            } else if (tablero[i][y] != '*') {
                break;
            }
        }
    
        // Verificar amenaza verticalmente hacia abajo
        for (int i = x + 1; i < n; i++) {
            if (tablero[i][y] == 'R') {
                amenaza = true;
                break;
            } else if (tablero[i][y] != '*') {
                break;
            }
        }
    
        if (amenaza)
            JOptionPane.showMessageDialog(null, "Esa ficha amenaza al rey");
        else
            JOptionPane.showMessageDialog(null, "Esa ficha NO amenaza al rey");
        break;

        
    }
    
    private void Alfil(){
        do{
            do{
                x = Integer.parseInt (JOptionPane.showInputDialog("Digite fila"));
                if(x<0 || x> n-1)
                    JOptionPane.showMessageDialog(null, "Esa fila esta por fuera");
            }
            while (x < 0 || x > n -1);
            do{
                x = Integer.parseInt (JOptionPane.showInputDialog("Digite columna"));
                if(y < 0 || y > n-1)
                    JOptionPane.showMessageDialog(null, "Esa columna esta por fuera");
            }
            while (y < 0 || y > n -1);

            if(tablero[x][y]== '*'){
                tablero[x][y]='C';
                break;
            }
            else 
                JOptionPane.showMessageDialog(null,"Casilla ya ocupada");
        }
        while(tablero[x][y] == '*');

        for(int i = 0; i < n; i ++){
            for (int j = 0; j < n; j ++){
                System.out.print(tablero[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("===================================");
        //evaluacion de amenazas
        //caso 1
        amenaza = false;
        contador = 1;
        f = x; 
        c = y; 

        while (f-contador>=0 && c+contador <n)//diagonal upright 
        {
            x = f-contador;
            y = c+contador;
            if(tablero[x][y]!= '*'){
                if(tablero[x][y] == 'R'){
                    amenaza=true;
                }
                else {
                    amenaza = false;
                }
                break;
            }
            contador++;
        }
        //caso 2
        contador = 1;
        if (!amenaza){
            while (f-contador>n && c+contador<n)//diagonal down right
            {
                x = f-contador;
                y = c+contador;
                if(tablero[x][y]!= '*'){
                    if(tablero[x][y] == 'R'){
                        amenaza=true;
                    }
                    else {
                        amenaza = false;
                    }
                    break;
                }
                contador++;
            }

        }
        //caso 3
        contador = 1;
        if (!amenaza){
            while (f+contador<n && c-contador>0)//diagonal downleft
            {
                x = f+contador;
                y = c-contador;
                if(tablero[x][y]!= '*'){
                    if(tablero[x][y] == 'R'){
                        amenaza=true;
                    }
                    else {
                        amenaza = false;
                    }
                    break;
                }
                contador++;
            }

        }
        //caso 4
        contador = 1;
        if (!amenaza){
            while (f-contador>0 && c-contador>0)//diagonal leftup
            {
                x = f- contador;
                y = c-contador;
                if(tablero[x][y]!= '*'){
                    if(tablero[x][y] == 'R'){
                        amenaza=true;
                    }
                    else {
                        amenaza = false;
                    }
                    break;
                }
                contador++;
            }

        }
        if(amenaza==true)
            JOptionPane.showMessageDialog(null, "Esa ficha amenaza al rey ");
        else
            JOptionPane.showMessageDialog(null, "Esa ficha NO amenaza al rey ");
    }

    private void Salir(){
            JOptionPane.showMessageDialog(null, "Gracias por jugar!");
            break;
            default:
                JOptionPane.showMessageDialog(null,"Opcion no valida!");
            break;
    }
}

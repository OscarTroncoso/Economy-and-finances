import javax.swing.JOptionPane;

public class Intervalo {
    public static void main (String[] args) {
        boolean Triqui = false, GO = false;
        int X, Y, Ronda = 1, CRonda = 0;
        char Sym;
        char[][] Tablero = new char[3][3];

        for(int i = 0; i < 3; i ++){
            for (int j = 0; j < 3; j ++){
                Tablero[i][j] = '*';
            }
        }
        do{
            do{
                JOptionPane.showMessageDialog(null, "Turno del jugador: " + Ronda);

                X = Integer.parseInt(JOptionPane.showInputDialog("Digite coordenada horizontal: "));
                Y = Integer.parseInt(JOptionPane.showInputDialog("Digite coordenada vertical: "));

                X = X - 1;
                Y = Y - 1;

                if(Ronda % 2 == 1){
                    Sym = 'O';
                    Ronda ++;
                } else {
                    Sym = 'X';
                    Ronda --;
                }

                Tablero[X][Y] = Sym;

                for(int i = 0; i < 3; i ++){
                    for (int j = 0; j < 3; j++){
                        System.out.println(Tablero[i][j]);
                    }
                }
                System.out.println("=======================0");

                for(int i = 0; i < 3; i ++){
                    if (Tablero[i][0] == Sym && Tablero[i][1] == Sym && Tablero[i][2] == Sym){
                        Triqui = true;            
                    }
                }
                for(int i = 0; i < 3; i ++){
                    if (Tablero[0][i] == Sym && Tablero[1][i] == Sym && Tablero[2][i] == Sym){
                        Triqui = true;            
                    }
                }
                if (Tablero[0][0] == Sym && Tablero[1][1] == Sym && Tablero[2][2] == Sym){
                    Triqui = true;            
                }
                if (Tablero[2][2] == Sym && Tablero[1][1] == Sym && Tablero[0][2] == Sym){
                    Triqui = true;            
                }

                if(Triqui == true){
                    GO = true;
                }
                Ronda ++;
            } 
            while(GO = false);
        }
    }
}
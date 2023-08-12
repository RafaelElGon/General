package RPG.lib;
import javax.swing.JOptionPane;
import java.util.Arrays;
import java.util.Scanner;

public class rpgDamage {
    public static void main(String[] args) {
        JOptionPane.showMessageDialog(null, ">>Bem vindo ao programa de cálculo de dano!<<");
        //JOptionPane.showMessageDialog(null, "");
        Scanner sc = new Scanner(System.in);

        System.out.println();
        System.out.println("Tipos de armas: ");
        String[] wpType = {"Arma de Força", "Arma Moderada", "Arma de Destreza"};

        for (String weaponType : wpType) { //Mostra tipos de armas
            System.out.print("["+ weaponType + "]"+" // ");
        }
        System.out.println();

        System.out.println("Classes de dano: ");
        String[] dmgType = {"Contudente", "Cortante", "Perfurante",
                "Cortante-Perfurante", "Contundente-Perfurante"};

        for (String damageType : dmgType) { //Mostra tipos de dano
            System.out.print("["+ damageType +"]" +" // ");
        }

        String leave = "";

        while (!leave.equals("x")) {
            String dmgClass = JOptionPane.showInputDialog("Classe do dano: ");

            if(!Arrays.asList(dmgType).contains(dmgClass)){
                while(!Arrays.asList(dmgType).contains(dmgClass.toLowerCase())){
                    dmgClass= JOptionPane.showInputDialog("Tipo de dano informado não " +
                                                            "corresponde, tente novamente: ");
                }
            }/* Verifica se a classe do dano informada pertence ao Array wpType, se não pertence
            pede para o usuário informar um tipo que pertença */

            //TODO: IMPLEMENTAR FÓRMULAS DE DANO
            System.out.println();
            leave = JOptionPane.showInputDialog("Para sair do programa, pressione x" +
                    "\nPara continuar no programa, pressione Enter");
            if(leave == null){
                leave = "x";
            }

            }
            System.out.println();

            //TALVEZ TRANSFORMAR EM UMA CLASSE?
        }
    }

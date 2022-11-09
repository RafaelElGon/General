package RPG.lib;


public class WeaponLib {
    private String [] weapons;

    public WeaponLib(String[] weapons) {
        this.weapons = weapons;
    }

    public boolean checkTypeinArray(String weaponType){
        for(String s: weapons){
            if(!s.equals(weaponType)){
                return false;
            }
        }
        return true;
    }
}

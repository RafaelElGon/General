package RPG.lib;

public class Weapon {
    private String weapon;
    private String damage;

    public Weapon(String weaponType, String damageType){
        this.weapon = weaponType;
        this.damage = damageType;
    }
    public Weapon(){
        this("", "");
    }
    public String getWeapon(){
        return this.weapon;
    }
    public String getDamage(){
        return this.damage;
    }
    public void setDamage(String dmg){
        this.damage = dmg;
    }
    public void setWeapon(String wp){
        this.weapon = wp;
    }
}

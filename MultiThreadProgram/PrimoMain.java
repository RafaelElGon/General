public class PrimoMain {
    public static void main(String[] args) {
        for(int i = 0; i<args.length; i++){
            PrimoThread t = new PrimoThread();
            int param = Integer.parseInt(args[i]);
            t.run(param);
        }
    }
}

public class PrimeThread extends Thread{
    private int taskID;

    public PrimeThread(int taskID) {
        this.taskId = taskID;
    }
    @Override
    public void run() {
        VerificaNumerosPrimos.test(taskID);
        System.out.println("Thread: " + Thread.currentThread().getName() + ", executando tarefa: " + taskID);
    }
}

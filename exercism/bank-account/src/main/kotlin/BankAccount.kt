class BankAccount {
    private var isOpen = true
    var balance: Long = 0
        get() { check(isOpen) ; return field }
        private set

    fun adjustBalance(amount: Long) {
        synchronized(this){
            balance += amount
        }  
    }

    fun close() {
        isOpen = false
    }
}
#include "atomic_counters.hpp"

atomic_counter_lock::atomic_counter_lock()
    : atomic_counter()
    , m_value(0)
    , m_lock() {
}

int atomic_counter_lock::increment() {
    //* loading and storing operations are locked
    m_lock.lock();
    int prev_value = m_value;
    m_value = m_value + 1;
    m_lock.unlock();
    return prev_value;
}

int atomic_counter_lock::decrement() {
    //* loading and storing operations are locked
    m_lock.lock();
    int prev_value = m_value;
    m_value = m_value - 1;
    m_lock.unlock();
    return prev_value;
}

void atomic_counter_lock::set(int value) {
    //* Storing operation is locked
    m_lock.lock();
    m_value = value;
    m_lock.unlock();
}

int atomic_counter_lock::get() {
    // TODO: Add locks here
    //* No need to lock the return statement as all other memory operations are locked
    // and also you cant lock return statement as program counter cannot reach the unlock statement after returning to calling function
    return m_value;
}

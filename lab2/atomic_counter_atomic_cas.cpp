#include "atomic_counters.hpp"

atomic_counter_atomic_cas::atomic_counter_atomic_cas()
    : atomic_counter()
    , m_value(0) {
}

int atomic_counter_atomic_cas::increment() {
    // int prev_value = m_value;
    // m_value = m_value + 1;
    // return prev_value;
    //* Load previous value atomically and replace the atomic value using atomic compare and exchange
    int prev_value = m_value.load();
    while(!m_value.compare_exchange_strong(prev_value, prev_value + 1)){}
    return prev_value;
}

int atomic_counter_atomic_cas::decrement() {
    // int prev_value = m_value;
    // m_value = m_value - 1;
    // return prev_value;
    //* Load previous value atomically and replace the atomic value using atomic compare and exchange
    int prev_value = m_value.load();
    while(!m_value.compare_exchange_strong(prev_value, prev_value - 1)){}
    return prev_value;
}

void atomic_counter_atomic_cas::set(int value) {
    //* Updating value using atomic store operation
    // m_value = value;
    m_value.store(value);
}

int atomic_counter_atomic_cas::get() {
    //* Returning value using atomic load operation
    return m_value.load();
}

#include "atomic_counters.hpp"

atomic_counter_atomic_incdec::atomic_counter_atomic_incdec()
    : atomic_counter()
    , m_value(0) {
}

int atomic_counter_atomic_incdec::increment() {
    //* Incrementing value using atomic fetch_add operation
    // int prev_value = m_value;
    // m_value = m_value + 1;
    // return prev_value;
    return m_value.fetch_add(1);
}

int atomic_counter_atomic_incdec::decrement() {
    //* Decrementing value using atomic fetch_sub operation
    // int prev_value = m_value;
    // m_value = m_value - 1;
    // return prev_value;
    return m_value.fetch_sub(1);
}

void atomic_counter_atomic_incdec::set(int value) {
    //* Updating value using atomic store operation
    // m_value = value;
    m_value.store(value);
}

int atomic_counter_atomic_incdec::get() {
    //* Returning value using atomic load operation
    return m_value.load();
}

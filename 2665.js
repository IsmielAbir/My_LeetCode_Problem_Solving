/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let pc = init;

    function increment(){
        return ++pc;
    }
    function decrement(){
        return --pc;
    }
    function reset(){
        return (pc=init);
    }

    return {increment, decrement, reset};
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
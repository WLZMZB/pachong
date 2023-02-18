
var buffer8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
var blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
var ARRAY_BUFFER = true
function Md5(t) {
    if (t)
        blocks[0] = blocks[16] = blocks[1] = blocks[2] = blocks[3] = blocks[4] = blocks[5] = blocks[6] = blocks[7] = blocks[8] = blocks[9] = blocks[10] = blocks[11] = blocks[12] = blocks[13] = blocks[14] = blocks[15] = 0,
            this.blocks = blocks,
            this.buffer8 = buffer8;
    else if (ARRAY_BUFFER) {
        var n = new ArrayBuffer(68);
        this.buffer8 = new Uint8Array(n),
            this.blocks = new Uint32Array(n)
    } else
        this.blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    this.h0 = this.h1 = this.h2 = this.h3 = this.start = this.bytes = this.hBytes = 0,
        this.finalized = this.hashed = !1,
        this.first = !0
}

var password = 123456

function main123(n) {
    // return new Md5(!0).update(n)[t]()
    return Md5(t)
}

console.log(main123(password))


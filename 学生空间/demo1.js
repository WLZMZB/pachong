var buffer = new ArrayBuffer(68);
buffer8 = new Uint8Array(buffer), blocks = new Uint32Array(buffer)
var ARRAY_BUFFER = true

function Md5(t) {
    if (t) blocks[0] = blocks[16] = blocks[1] = blocks[2] = blocks[3] = blocks[4] = blocks[5] = blocks[6] = blocks[7] = blocks[8] = blocks[9] =
        blocks[10] = blocks[11] = blocks[12] = blocks[13] = blocks[14] = blocks[15] = 0, this.blocks = blocks, this.buffer8 = buffer8;
    else if (ARRAY_BUFFER) {
        var n = new ArrayBuffer(68);
        this.buffer8 = new Uint8Array(n), this.blocks = new Uint32Array(n)
    } else this.blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    this.h0 = this.h1 = this.h2 = this.h3 = this.start = this.bytes = this.hBytes = 0, this.finalized = this.hashed = !1, this.first = !0
}
//Md5.prototype.update =
var ERROR="input is invalid type"
var SHIFT = [0, 8, 16, 24]
function update(t) {
    if (!this.finalized) {
        var n, e = typeof t;
        if ("string" !== e) {
            if ("object" !== e)
                throw ERROR;
            if (null === t)
                throw ERROR;
            if (ARRAY_BUFFER && t.constructor === ArrayBuffer)
                t = new Uint8Array(t);
            else if (!(Array.isArray(t) || ARRAY_BUFFER && ArrayBuffer.isView(t)))
                throw ERROR;
            n = !0
        }
        for (var r, o, i = 0, u = t.length, c = this.blocks, a = this.buffer8; i < u; ) {
            if (this.hashed && (this.hashed = !1,
            c[0] = c[16],
            c[16] = c[1] = c[2] = c[3] = c[4] = c[5] = c[6] = c[7] = c[8] = c[9] = c[10] = c[11] = c[12] = c[13] = c[14] = c[15] = 0),
            n)
                if (ARRAY_BUFFER)
                    for (o = this.start; i < u && o < 64; ++i)
                        a[o++] = t[i];
                else
                    for (o = this.start; i < u && o < 64; ++i)
                        c[o >> 2] |= t[i] << SHIFT[3 & o++];
            else if (ARRAY_BUFFER)
                for (o = this.start; i < u && o < 64; ++i)
                    (r = t.charCodeAt(i)) < 128 ? a[o++] = r : r < 2048 ? (a[o++] = 192 | r >> 6,
                    a[o++] = 128 | 63 & r) : r < 55296 || r >= 57344 ? (a[o++] = 224 | r >> 12,
                    a[o++] = 128 | r >> 6 & 63,
                    a[o++] = 128 | 63 & r) : (r = 65536 + ((1023 & r) << 10 | 1023 & t.charCodeAt(++i)),
                    a[o++] = 240 | r >> 18,
                    a[o++] = 128 | r >> 12 & 63,
                    a[o++] = 128 | r >> 6 & 63,
                    a[o++] = 128 | 63 & r);
            else
                for (o = this.start; i < u && o < 64; ++i)
                    (r = t.charCodeAt(i)) < 128 ? c[o >> 2] |= r << SHIFT[3 & o++] : r < 2048 ? (c[o >> 2] |= (192 | r >> 6) << SHIFT[3 & o++],
                    c[o >> 2] |= (128 | 63 & r) << SHIFT[3 & o++]) : r < 55296 || r >= 57344 ? (c[o >> 2] |= (224 | r >> 12) << SHIFT[3 & o++],
                    c[o >> 2] |= (128 | r >> 6 & 63) << SHIFT[3 & o++],
                    c[o >> 2] |= (128 | 63 & r) << SHIFT[3 & o++]) : (r = 65536 + ((1023 & r) << 10 | 1023 & t.charCodeAt(++i)),
                    c[o >> 2] |= (240 | r >> 18) << SHIFT[3 & o++],
                    c[o >> 2] |= (128 | r >> 12 & 63) << SHIFT[3 & o++],
                    c[o >> 2] |= (128 | r >> 6 & 63) << SHIFT[3 & o++],
                    c[o >> 2] |= (128 | 63 & r) << SHIFT[3 & o++]);
            this.lastByteIndex = o,
            this.bytes += o - this.start,
            o >= 64 ? (this.start = o - 64,
            this.hash(),
            this.hashed = !0) : this.start = o
        }
        return this.bytes > 4294967295 && (this.hBytes += this.bytes / 4294967296 << 0,
        this.bytes = this.bytes % 4294967296),
        this
    }
}
var password = 123456
function I(e) {
            var t = c(e).toUpperCase()
              , n = r(t).toUpperCase();}

function main123(n) {
    return new Md5(!0).update(n)[t]()
    // return Md5(n)
}

console.log(main123(password))


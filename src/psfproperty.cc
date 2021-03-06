#include "psf.h"
#include "psfdata.h"
#include "psfinternal.h"

Property::~Property() {
    if(value) 
	delete(value);
}

Property::Property(Property const &x) {
    if(x.value) {
	name = x.name;
	value = x.value->clone();
    } else
	value = NULL;
}

int Property::deserialize(const char *buf) {
    const char *startbuf = buf;

    chunktype = GET_INT32(buf);
    buf += 4;

    if(!ischunk(chunktype))
	throw IncorrectChunk(chunktype);

    buf += name.deserialize(buf);

    switch(chunktype) {
    case 33:
	value = new PSFStringScalar;
	buf += value->deserialize(buf);
	break;
    case 34:
	value = new PSFInt32Scalar();
	buf += value->deserialize(buf);
	break;
    case 35:
	value = new PSFDoubleScalar();
	buf += value->deserialize(buf);
	break;
    }
    return buf - startbuf;
}


#
# Copyright 2011  Vincent Batts, Vienna, VA, USA
# All rights reserved.
#
# Redistribution and use of this script, with or without modification, is
# permitted provided that the following conditions are met:
#
# 1. Redistributions of this script must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

'''
        A typical "task" (using lots of functionality), looks like:
        {   u'id': u'<redacted hash>',
                      u'kind': u'tasks#task',
                      u'position': u'00000000000000001388',
                      u'notes': u'Sitting in the basket',
                      u'selfLink': u'https://www.googleapis.com/tasks/v1/lists/<redacted hash>/tasks/<redacted hash>',
                      u'status': u'needsAction',
                      u'title': u'library book drop off',
                      u'due': u'2011-09-07T00:00:00.000Z',
                      u'updated': u'2011-08-14T15:55:36.625Z'}
'''
class pygtask(object):
    __attrs = {}

    def __init__(self, gtask=None, options={}):
        None

    # Simple return of "kind"
    def kind(self):
        return self.__get_attr(u'kind')

    # Simple return of "position"
    def position(self):
        return self.__get_attr(u'position')

    # Simple return of "notes"
    def notes(self):
        return self.__get_attr(u'notes')

    # Simple return of "selfLink"
    def selfLink(self):
        return self.__get_attr(u'selfLink')

    # Simple return of "status"
    def status(self):
        return self.__get_attr(u'status')

    # Simple return of "title"
    def title(self):
        return self.__get_attr(u'title')

    # Simple return of "due"
    def due(self):
        return self.__get_attr(u'due')

    # Simple return of "updated"
    def updated(self):
        return self.__get_attr(u'updated')

    # Simple return of "parent"
    def parent(self):
        return self.__get_attr(u'parent')

    # An internal getter
    def __get_attr(self, attr):
        if (self.__attrs.has_key(attr)):
            return self.__attrs[attr]
        else:
            return None



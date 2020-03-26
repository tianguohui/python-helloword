#!/usr/bin/python
# coding=utf-8
import redis


class CRedis:
    def __init__(self):
        self.host = '10.1.13.17'
        self.port = 31009
        self.db = 0
        self.r = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

    # 1. strings ���ͼ�����
    # ���� key ��Ӧ��ֵΪ string ���͵� value
    def set(self, key, value):
        return self.r.set(key, value)

    # ���� key ��Ӧ��ֵΪ string ���͵� value����� key �Ѿ�����,���� 0,nx �� not exist ����˼
    def setnx(self, key, value):
        return self.r.setnx(key, value)

    # ���� key ��Ӧ��ֵΪ string ���͵� value,��ָ���˼�ֵ��Ӧ����Ч��
    def setex(self, key, time, value):
        return self.r.setex(key, time, value)

    # ����ָ�� key �� value ֵ�����ַ���
    # setrange name 8 gmail.com
    # ���е� 8 ��ָ���±�Ϊ 8(���� 8)���ַ���ʼ�滻
    def setrange(self, key, num, value):
        return self.r.setrange(key, num, value)

    # ��ȡָ�� key �� value ֵ�����ַ���
    def getrange(self, key, start, end):
        return self.r.getrange(key, start, end)

    # mget(list)
    def get(self, key):
        if isinstance(key, list):
            return self.r.mget(key)
        else:
            return self.r.get(key)

    # ɾ��
    def remove(self, key):
        return self.r.delete(key)

    # ����
    def incr(self, key, default=1):
        if (1 == default):
            return self.r.incr(key)
        else:
            return self.r.incr(key, default)

    # �Լ�
    def decr(self, key, default=1):
        if (1 == default):
            return self.r.decr(key)
        else:
            return self.r.decr(key, default)

    # 2. hashes ���ͼ�����
    # ����email��ȡsession��Ϣ
    def hget(self, email):
        return self.r.hget('session', email)

    # ��email��ΪΨһ��ʶ�������û�session
    def hset(self, email, content):
        return self.r.hset('session', email, content)

    # ��ȡsession��ϣ���е���������
    def hgetall(self):
        return self.r.hgetall('session')

    # ɾ��hashes
    def hdel(self, name, key=None):
        if (key):
            return self.r.hdel(name, key)
        return self.r.hdel(name)

    # ��յ�ǰdb
    def clear(self):
        return self.r.flushdb()

    # 3��lists ���ͼ�����
    # �ʺ����ʼ�����
    # �� key ��Ӧ list ��ͷ������ַ���Ԫ��
    def lpush(self, key, value):
        return self.r.lpush(key, value)

    # �� list ��β��ɾ��Ԫ��,������ɾ��Ԫ��
    def lpop(self, key):
        return self.r.plush(key)


if __name__ == '__main__':
    r = CRedis()
    print (r.get("id"))
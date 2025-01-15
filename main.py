class Event:
    def _init_(self, name, payload=None):
        self.name = name
        self.payload = payload or {}

class OrderSubmittedEvent(Event):
    def _init_(self, order_id, customer_id):
        super()._init_("OrderSubmitted", {"order_id": order_id, "customer_id": customer_id})

class OrderRejectedEvent(Event):
    def _init_(self, order_id, reason):
        super()._init_("OrderRejected", {"order_id": order_id, "reason": reason})

class CommunicationQueue:
    def _init_(self):
        self.queue = []

     def add_event(self, event):
        print(f"Event added: {event.name}")
        self.queue.append(event)

     def process_events(self):
        while self.queue:
            event = self.queue.pop(0)
            print(f"Processing event: {event.name}, Payload: {event.payload}")

class Store:
    def _init_(self, queue):
        self.queue = queue

    def submit_order(self, order_id, customer_id):
        print(f"Submitting order: {order_id} for customer {customer_id}")
        event = OrderSubmittedEvent(order_id, customer_id)
        self.queue.add_event(event)

    def reject_order(self, order_id, reason):
        print(f"Rejecting order: {order_id}, Reason: {reason}")
        event = OrderRejectedEvent(order_id, reason)
        self.queue.add_event(event)

class Customer:
    def _init_(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def place_order(self, store, order_id):
        print(f"{self.name} is placing an order: {order_id}")
        store.submit_order(order_id, self.customer_id)


if _name_ == "_main_":
    queue = CommunicationQueue()
    store = Store(queue)
    queue = CommunicationQueue()
    store = Store(queue)

customer1 = Customer(1,"selma")
customer2 = Customer(2,"ayse")

customer1.place_order(store, "ORD001")
customer2.place_order(store, "ORD002")


queue.process_events()






